#include <stdio.h>

int main()
{
	int a, b;
	while (1 == scanf("%d", &a)) {
		long pos = ftell(stdin);
		while (1 == scanf("%d", &b))
			if (a+b == 2020) {
				printf("%d\n", a*b);
				return 0;
			}
		fseek(stdin, pos, SEEK_SET);
	}
}
