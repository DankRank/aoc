#include <stdio.h>

int main()
{
	long maskor = 0, maskand = ~0;
	long mem[65536] = {0};
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
				case '0': maskand |= 1; break;
				}
			}
			maskand = ~maskand;
		} else if (k1 > 0) {
			long addr = 0, data = 0;
			if (2 != scanf("em[%ld] = %ld", &addr, &data))
				fprintf(stderr, "uh oh\n");
			mem[addr] = (data&maskand) | maskor;
		} else {
			break;
		}
	}
	long sum = 0;
	for (int i = 0; i < 65536; i++)
		sum += mem[i];
	printf("%ld\n", sum);
}
