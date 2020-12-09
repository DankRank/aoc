#include <stdio.h>
#define N 25
int main()
{
	long set[1000] = {0};
	int i = 0;
	while (i < N)
		scanf("%ld",&set[i++]);
	while (1 == scanf("%ld",&set[i++]))
		;
	for (int j = N; j < i; j++) {
		for (int u = j-N; u < j; u++)
			for (int v = u+1; v < j; v++)
				if (set[j] == set[u]+set[v])
					goto found;
		printf("%ld\n", set[j]);
		break;
	found:;
	}
}
