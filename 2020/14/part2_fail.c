#include <stdio.h>
struct decode_rule {
	long mask;
	long base;
	long value;
};
struct decode_rule rules[600] = {0};
int nrules = 0;
long decode(long addr) {
	for (int i = nrules-1; i >= 0; i--)
		if ((addr&rules[i].mask) == rules[i].base)
			return rules[i].value;
	return 0;
}

int main()
{
	long maskor = 0, maskand = ~0;
	for (;;) {
		int k1 = 0, k2 = 0;
		scanf(" m%na%nsk = ", &k1, &k2);
		if (k2 > 0) {
			maskor = 0;
			maskand = 0;
			for (int i=0; i<36; i++) {
				maskor <<= 1;
				maskand <<= 1;
				switch (getchar()) {
				case '1': maskor |= 1; break;
				case 'X': maskand |= 1; break;
				}
			}
			maskand = ~maskand;
		} else if (k1 > 0) {
			long addr = 0, data = 0;
			if (2 != scanf("em[%ld] = %ld", &addr, &data))
				fprintf(stderr, "uh oh\n");
			rules[nrules].mask = maskand;
			rules[nrules].base = (addr&maskand) | maskor;
			rules[nrules].value = data;
			nrules++;
		} else {
			break;
		}
	}
	long sum = 0;
	for (long i = 0; i < (1L<<36); ) {
		for (long j = 0; j < (1L<<20); i++, j++)
			sum += decode(i);
		printf("%ld/65536\n",i>>20);
	}
	printf("%ld\n", sum);
}
