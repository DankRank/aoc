#include <stdio.h>
#include "ht.c"

int main()
{
	/* rehashing code isn't particularly stable atm, so i set the bucket size high */
	struct ht *ht = ht_create((ht_params){.nbuckets=1});
	long maskor = 0, maskand = ~0;
	int prem = 0;
	for (;;) {
		int k1 = 0, k2 = 0;
		scanf(" m%na%nsk = ", &k1, &k2);
		if (k2 > 0) {
			maskor = 0;
			maskand = 0;
			prem = 0;
			for (int i=0; i<36; i++) {
				maskor <<= 1;
				maskand <<= 1;
				switch (getchar()) {
				case '1': maskor |= 1; break;
				case 'X': maskand |= 1; prem++; break;
				}
			}
			maskand = ~maskand;
		} else if (k1 > 0) {
			long addr = 0, data = 0;
			if (2 != scanf("em[%ld] = %ld", &addr, &data))
				fprintf(stderr, "uh oh\n");
			addr = (addr&maskand) | maskor;

			for (long i = 0; i < (1<<prem); i++) {
				long p = i;
				long pkey = addr;
				for (int j = 0; j < 36; j++)
					if (!(maskand>>j & 1)) {
						pkey |= (p&1)<<j;
						p >>= 1;
					}
				ht_put(ht, (void*)(pkey+1), (void*)data);
			}
		} else {
			break;
		}
	}
	long sum = 0;
	void *value;
	for (ht_iter it = {ht,0}; ht_next(NULL, &value, &it); )
		sum += (long)value;
	printf("%ld\n", sum);
	ht_free(ht);
}
