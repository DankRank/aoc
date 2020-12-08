#include <stdio.h>

int main()
{
	int sum = 0;
	int n;
	int c;
	while ((c = getchar()) != EOF) {
		if (c == '-' || (c >= '0' && c <= '9')) {
			ungetc(c, stdin);
			scanf("%d",&n);
			sum += n;
		}
	}
	printf("%d\n", sum);
}
