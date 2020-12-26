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
int is_edge(int x);
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
				b |= 1;
			if (p[9][9-i] == '#')
				c |= 1;
			if (p[9-i][0] == '#')
				d |= 1;
		}
		int w = is_edge(canonical(a));
		int x = is_edge(canonical(b));
		int y = is_edge(canonical(c));
		int z = is_edge(canonical(d));

		if (2 == w+x+y+z) {
			printf("%s", buf);
			if (w)
				printf("a %d\n", a);
			if (x)
				printf("b %d\n", b);
			if (y)
				printf("c %d\n", c);
			if (z)
				printf("d %d\n", d);
		}
		fgets(buf, 512, stdin);
	}
}
int is_edge(int x)
{
	switch (x) { case 101: case 107: case 110: case 118: case 139: case 145: case 148: case 174: case 19: case 190: case 2: case 205: case 213: case 22: case 24: case 243: case 25: case 26: case 271: case 273: case 309: case 310: case 33: case 337: case 346: case 371: case 439: case 445: case 489: case 49: case 535: case 539: case 559: case 567: case 573: case 587: case 595: case 619: case 621: case 623: case 631: case 723: case 747: case 75: case 751: case 795: case 855: case 919: return 1; }
	return 0;
}
