#include <stdio.h>

int main()
{
	unsigned char space[256][32] = {{1}};
	unsigned char x=0, y=0;
	int total = 1;
	int c;
	while (EOF != (c = getchar())) {
		if (c == '<')
			x--;
		if (c == '>')
			x++;
		if (c == '^')
			y--;
		if (c == 'v')
			y++;

		if (!(space[y][x>>3] & 1<<(x&7)))
			total++;
		space[y][x>>3] |= 1<<(x&7);
	}

	printf("%d\n", total);
}
