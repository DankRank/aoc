#include <stdio.h>
#include <assert.h>

int main()
{
	int timestart;
	scanf("%d ", &timestart);
	int set[100];
	int n = 0;
	for (;;) {
		if (1 != scanf("%d,", &set[n])) {
			int test = 0;
			scanf("x%n,",&test);
			if (test != 1)
				break;
			set[n] = 0;
		}
		n++;
	}
	struct {
		int off,val;
	} cset[100];
	int m = 0;
	int k = 0;
	for (int i = 0; i < n; i++) {
		if (set[i]) {
			cset[m].off = k;
			cset[m].val = set[i];
			m++;
		}
		k++;
	}
	for (int i = 0; i < m; i++) {
		printf("(i+%d)%%%d == 0\n", cset[i].off, cset[i].val);
	}
#if 0
	assert(!cset[0].off);
	for (long i = 0; ; i += cset[0].val) {
		for (int j = 1; j < m; j++)
			if ((i+cset[j].off)%cset[j].val)
				goto next;
		printf("%ld\n",i);
		return 0;
		next:;
	}
#endif
}
