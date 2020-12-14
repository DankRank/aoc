#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include "ht.h"

#ifndef HT_FASTMOD
#	if defined(__SIZEOF_INT128__)
#		define HT_FASTMOD 1
#	else
#		define HT_FASTMOD 0
#	endif
#endif
#if HT_FASTMOD
#include <stdint.h>
/* arXiv:1902.01961 */
static inline uint64_t fastmod_compute_c(size_t d)
{
	if (d <= UINT32_MAX)
		return UINT64_C(0xFFFFFFFFFFFFFFFF) / d + 1;
	else
		return 0;
}
static inline size_t fastmod(size_t n, uint64_t c, size_t d)
{
	if (c) {
		uint64_t lowbits = c * n;
		return ((__uint128_t)lowbits * d) >> 64;
	}
	return n % d;
}
#endif

struct kv {
	void *key, *value;
};
struct ht {
	size_t nbuckets;
	struct kv *buckets;
	size_t maxload;
	size_t total;
	size_t (*hash)(void *key);
	int (*compare)(void *lhs, void *rhs);
	void (*free_key)(void *key);
	void (*free_value)(void *key);
	int dont_abort;
#if HT_FASTMOD
	uint64_t fastmod_c;
#endif
};

static const size_t primes[] = {
	11, 23, 53, 97,
	193, 389, 769, 1543,
	3079, 6151, 12289, 24593,
	49157, 98317, 196613, 393241,
	786433, 1572869, 3145739, 6291469,
	12582917, 25165843, 50331653, 100663319,
	201326611, 402653189, 805306457, 1610612741,
};

static void set_next_cap(struct ht *ht, size_t cap)
{
	for (size_t i = 0; i < sizeof(primes)/sizeof(primes[0]); i++) {
		if (primes[i] > cap) {
			ht->nbuckets = primes[i];
			goto brk;
		}
	}
	/* this allows us to set the initial cap with set_next_cap(ht,cap&~1) */
	ht->nbuckets = cap&1 ? cap*2+1 : cap+1;
brk:;
#if HT_FASTMOD
	ht->fastmod_c = fastmod_compute_c(ht->nbuckets);
#endif
	ht->maxload = (ht->nbuckets>>2) + (ht->nbuckets>>1); /* 75% */
}

static size_t hash(struct ht *ht, void *key)
{
	size_t h = ht->hash ? (size_t)ht->hash(key) : (size_t)key;
#if HT_FASTMOD
	return fastmod(h, ht->fastmod_c, ht->nbuckets);
#else
	return h % ht->nbuckets;
#endif
}
static int compare(struct ht *ht, void *lhs, void *rhs)
{
	return lhs != rhs && (!ht->compare || ht->compare(lhs, rhs));
}

#define abort_or(cond, val) ((void)((cond) && (abort(),0)), (val))
struct ht *ht_create(ht_params params)
{
	struct ht *ht;
	ht = calloc(1, sizeof(struct ht));
	if (!ht)
		return abort_or(!params.dont_abort, NULL);

	set_next_cap(ht, params.nbuckets&~1);
	ht->buckets = calloc(ht->nbuckets, sizeof(struct kv));
	if (!ht->buckets) {
		free(ht);
		return abort_or(!params.dont_abort, NULL);
	}
	ht->total = 0;
	ht->hash = params.hash;
	ht->compare = params.compare;
	ht->free_key = params.free_key;
	ht->free_value = params.free_value;
	ht->dont_abort = params.dont_abort;

	return ht;
}
static void free_kv(struct ht *ht, struct kv *kv)
{
	if (ht->free_key)
		ht->free_key(kv->key);
	if (ht->free_value)
		ht->free_value(kv->value);
	kv->key = kv->value = NULL;
}
void ht_free(struct ht *ht)
{
	if (!ht)
		return;
	if (ht->free_key || ht->free_value)
		for (size_t i = 0; i < ht->nbuckets; i++)
			free_kv(ht, &ht->buckets[i]);
	free(ht->buckets);
	free(ht);
}
static int rehash(struct ht *ht)
{
	if (ht->total < ht->maxload)
		return 0;
	size_t nbuckets = ht->nbuckets;
	set_next_cap(ht, nbuckets);
	size_t nbuckets2 = ht->nbuckets;

	struct kv *buckets = ht->buckets;
	struct kv *buckets2 = calloc(nbuckets2, sizeof(struct kv));
	if (!buckets2) {
		set_next_cap(ht, nbuckets-1);
		return abort_or(!ht->dont_abort, -1);
	}
	for (size_t i = 0; i < nbuckets; i++)
		if (buckets[i].key) {
			size_t h = hash(ht, buckets[i].key);
			for (size_t j = h; ; ) {
				if (!buckets2[j].key) {
					buckets2[j] = buckets[i];
					break;
				}
				if (++j == nbuckets2)
					j = 0;
				if (j == h)
					abort();
			}
		}

	free(buckets);
	ht->buckets = buckets2;
	return 0;
}
static struct kv *find_kv(struct ht *ht, void *key)
{
	size_t h = hash(ht, key);

	for (size_t i = h; ; ) {
		if (!ht->buckets[i].key || !compare(ht, key, ht->buckets[i].key))
			return &ht->buckets[i];
		if (++i == ht->nbuckets)
			i = 0;
		if (i == h)
			abort();
	}
}
int ht_contains(struct ht *ht, void *key, void **out)
{
	assert(ht);
	struct kv *kv = find_kv(ht, key);
	if (out)
		*out = kv->key ? kv->value : NULL;
	return !!kv->key;
}
void *ht_get(struct ht *ht, void *key)
{
	void *rv;
	ht_contains(ht, key, &rv);
	return rv;
}
int ht_put(struct ht *ht, void *key, void *value)
{
	assert(ht);
	if (rehash(ht))
		return -1;
	struct kv *kv = find_kv(ht, key);
	if (kv->key)
		free_kv(ht, kv);
	kv->key = key;
	kv->value = value;
	ht->total++;
	return 0;
}
int ht_remove(struct ht *ht, void *key)
{
	assert(ht);
	struct kv *kv = find_kv(ht, key);
	if (!kv->key)
		return 0;
	free_kv(ht, kv);
	ht->total--;

	size_t h = kv - ht->buckets;
	size_t i = h;
	size_t j = h;
	for (;;) {
		if (j++ == ht->nbuckets)
			j = 0;
		if (j == h)
			abort();
		if (!ht->buckets[j].key) {
			ht->buckets[i].key = NULL;
			ht->buckets[i].value = NULL;
			break;
		}
		size_t k = hash(ht, ht->buckets[j].key);
		if (i <= j ? (k <= i || j < k) : (j < k && k <= i)) {
			ht->buckets[i] = ht->buckets[j];
			i = j;
		}
	}
	return 0;
}
size_t ht_count(struct ht *ht)
{
	assert(ht);
	return ht->total;
}
int ht_next(void **key, void **value, ht_iter *it)
{
	assert(it);
	struct ht *ht = it->ht;
	assert(ht);
	for (;; it->pos++) {
		if (it->pos >= ht->nbuckets) {
			it->pos = 0;
			return 0;
		}
		if (ht->buckets[it->pos].key) {
			break;
		}
	}
	struct kv *kv = &ht->buckets[it->pos++];
	if (key)
		*key = kv->key;
	if (value)
		*value = kv->value;
	return 1;
}

size_t ht_strhash(void *key)
{
	const char *s = key;
	/* FNV-1a */
#if SIZE_MAX > 4294967295u
	size_t h = 14695981039346656037u;
	while (*s)
		h = (h^*s++) * 1099511628211u;
#else
	size_t h = 2166136261u;
	while (*s)
		h = (h^*s++) * 16777619u;
#endif
	return h;
}
int ht_strcmp(void *lhs, void *rhs)
{
	return !!strcmp(lhs, rhs);
}
