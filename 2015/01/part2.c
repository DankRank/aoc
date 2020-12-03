#include <stdio.h>
int main()
{
	int c;
	int floor = 0;
	int pos = 0;
	while (EOF != (c = getchar())) {
		if (c == '(')
			floor++, pos++;
		if (c == ')')
			floor--, pos++;
		if (floor == -1) {
			printf("%d\n", pos);
			return 0;
		}
	}
}
