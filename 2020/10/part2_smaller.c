#include <stdio.h>
#include <stdlib.h>
int compare(const void *lhs, const void *rhs)
{
	return *(const int *)lhs - *(const int *)rhs;
}
int main()
{
	int set[100] = {0};
	int n = 1;
	while (1 == scanf("%d", &set[n]))
		n++;

	qsort(set, n, sizeof(int), compare);
	set[n] = set[n-1] + 3;
	n++;

	long total = 1;
	int i=0, j=1;
	while (i < n-1) {
		while (j < n-1 && set[j+1]-set[j-1] < 4)
			j++;
		switch (j-i-1) {
		case 0: break;
		case 1: total *= 2; break;
		case 2: total *= 7 - (set[j]-set[i]); break;
		case 3: total *= 11 - (set[j]-set[i]); break;
		default:
			printf("unsupported %d\n", n);
			abort();
		}
		i = j++;
	}
	printf("%ld\n", total);
}
