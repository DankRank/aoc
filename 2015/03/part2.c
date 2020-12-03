#include <stdio.h>

int main()
{
	unsigned char space[256][32] = {{1}};
	unsigned char x1=0, y1=0, x2=0, y2=0;
	int total = 1;
	int c;
	while (EOF != (c = getchar())) {
		if (c == '<')
			x1--;
		if (c == '>')
			x1++;
		if (c == '^')
			y1--;
		if (c == 'v')
			y1++;

		if (!(space[y1][x1>>3] & 1<<(x1&7)))
			total++;
		space[y1][x1>>3] |= 1<<(x1&7);

		c = getchar();
		if (c == EOF)
			break;

		if (c == '<')
			x2--;
		if (c == '>')
			x2++;
		if (c == '^')
			y2--;
		if (c == 'v')
			y2++;

		if (!(space[y2][x2>>3] & 1<<(x2&7)))
			total++;
		space[y2][x2>>3] |= 1<<(x2&7);
	}

	printf("%d\n", total);
}
