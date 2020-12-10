#include <stdio.h>
#include <stdlib.h>
static inline int is_fixed(int *p)
{
	return p[1]-p[-1] >= 4;
	/* return (p[0] - p[-1] == 2 && p[1] - p[0] == 2) || p[0] - p[-1] == 3 || p[1] - p[0] == 3; */
}
/*
 * 1 = 1
 * 2 = 1
 * 11 = 2
 * 12 = 2
 * 21 = 2
 * 111 = 4
 * 112 = 3
 * 121 = 3
 * 211 = 3
 * 212 = 3
 * 1111 = 7
 * 1112 = 6
 * 1121 = 6
 * 1211 = 6
 * 1212 = 5
 * 2111 = 6
 * 2112 = 5
 * 2121 = 5
 */
static inline int microsolver(int *p, int n)
{
	switch (n) {
	case 0:
		return 1;
	case 1:
		return 2;
	case 2:
		return 7 - (p[3]-p[0]); /* returns 4 or 3 */
	case 3:
		return 11 - (p[4]-p[0]); /* returns 7 or 6 or 5 */
	default:
		printf("unsupported %d\n", n);
		abort();
	}
}
static long macrosolver(int set[], int n)
{
	long total = 1;
	int i=0, j=1;
	while (i < n-1) {
		while (j < n-1 && !is_fixed(&set[j]))
			j++;
		total *= microsolver(&set[i], j-i-1);
		i = j++;
	}
	return total;
}


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

	printf("%ld\n", macrosolver(set, n));
}
