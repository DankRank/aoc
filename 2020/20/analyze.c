#include <stdio.h>
int reversal(int x)
{
	int y = 0;
	for (int i = 0; i < 10; i++) {
		y <<= 1;
		if (x&1)
			y |= 1;
		x >>= 1;
	}
	return y;
}
int canonical(int x)
{
	int y = reversal(x);
	return y < x ? y : x;
}
int main()
{
	char buf[512];
	char p[10][12];
	while (fgets(buf, 512, stdin)) {
		for (int i = 0; i < 10; i++)
			fgets(p[i], 12, stdin);

		int a = 0, b = 0, c = 0, d = 0;
		for (int i = 0; i < 10; i++) {
			a <<= 1;
			b <<= 1;
			c <<= 1;
			d <<= 1;
			if (p[0][i] == '#')
				a |= 1;
			if (p[i][9] == '#')
				c |= 1;
			if (p[9][9-i] == '#')
				b |= 1;
			if (p[9-i][0] == '#')
				d |= 1;
		}
		printf("%d\n%d\n%d\n%d\n", canonical(a), canonical(b), canonical(c), canonical(d));
		fgets(buf, 512, stdin);
	}
}
