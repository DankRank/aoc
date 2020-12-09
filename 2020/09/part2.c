#include <stdio.h>
#include <limits.h>
#define TARGET 70639851
int main()
{
	long set[1000] = {0};
	int i = 0, j = 0, k = 0;
	while (1 == scanf("%ld",&set[i++]))
		;
	for (j = 0; j < i; j++) {
		long sum = 0;
		for (k = j; k < i ; k++) {
			sum += set[k];
			if (sum == TARGET)
				goto found;
			if (sum > TARGET)
				break;
		}
	}
	printf("not found\n");
	return 1;
found:;
	long max = LONG_MIN;
	long min = LONG_MAX;
	for (; j < k; j++) {
		if (set[j] > max)
			max = set[j];
		if (set[j] < min)
			min = set[j];
	}
	printf("%ld\n", min+max);
}
