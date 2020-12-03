#include <stdio.h>
int main()
{
	int c;
	int floor = 0;
	while (EOF != (c = getchar())) {
		if (c == '(')
			floor++;
		if (c == ')')
			floor--;
	}
	printf("%d\n", floor);
}
