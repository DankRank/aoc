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

	int diffs[4] = {0};
	for (int i = 1; i < n; i++)
		diffs[set[i] - set[i-1]]++;
	printf("%d\n", diffs[1]*diffs[3]);
}
