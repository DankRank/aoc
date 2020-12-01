#include <stdio.h>

int main()
{
	int a, b, c;
	while (1 == scanf("%d", &a)) {
		long pos = ftell(stdin);
		while (1 == scanf("%d", &b)) {
			long pos2 = ftell(stdin);
			while (1 == scanf("%d", &c))
				if (a+b+c == 2020) {
					printf("%d\n", a*b*c);
					return 0;
				}
			fseek(stdin, pos2, SEEK_SET);
		}
		fseek(stdin, pos, SEEK_SET);
	}
}
