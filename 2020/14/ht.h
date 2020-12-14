#ifndef HT_H_
#define HT_H_
#include <stddef.h>
struct ht;
typedef struct _ht_params_tag {
	size_t nbuckets;
	size_t (*hash)(void *key);
	int (*compare)(void *lhs, void *rhs);
	void (*free_key)(void *key);
	void (*free_value)(void *key);
	int dont_abort;
} ht_params;
typedef struct _ht_iter_tag { struct ht *ht; size_t pos; } ht_iter;

struct ht *ht_create(ht_params params);
void ht_free(struct ht *ht);
int ht_contains(struct ht *ht, void *key, void **out);
void *ht_get(struct ht *ht, void *key);
int ht_put(struct ht *ht, void *key, void *value);
int ht_remove(struct ht *ht, void *key);
size_t ht_count(struct ht *ht);
int ht_next(void **key, void **value, ht_iter *it);

size_t ht_strhash(void *key);
int ht_strcmp(void *lhs, void *rhs);
#endif
