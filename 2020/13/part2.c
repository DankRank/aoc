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
	long i = 0;
	long a = 1;
	for (int d = 0; d < n; d++) {
		if (set[d]) {
			while ((i+d)%set[d] != 0)
				i += a;
			a *= set[d];
		}
	}
	printf("%ld\n",i);
}
