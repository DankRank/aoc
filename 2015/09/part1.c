#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

enum {
	AlphaCentauri = 0,
	Arbre,
	Faerun,
	Norrath,
	Snowdin,
	Straylight,
	Tambi,
	Tristram
};

int destid(const char *p)
{
	if (!strcmp(p, "AlphaCentauri"))
		return AlphaCentauri;
	if (!strcmp(p, "Arbre"))
		return Arbre;
	if (!strcmp(p, "Faerun"))
		return Faerun;
	if (!strcmp(p, "Norrath"))
		return Norrath;
	if (!strcmp(p, "Snowdin"))
		return Snowdin;
	if (!strcmp(p, "Straylight"))
		return Straylight;
	if (!strcmp(p, "Tambi"))
		return Tambi;
	if (!strcmp(p, "Tristram"))
		return Tristram;
	abort();
}

int main()
{
	char buf1[64], buf2[64];
	int tab[8][8] = {0};
	int dist;
	while (3 == scanf("%63s to %63s = %d", buf1, buf2, &dist)) {
		int d1 = destid(buf1);
		int d2 = destid(buf2);
		tab[d1][d2] = tab[d2][d1] = dist;
	}
	int shortest = INT_MAX;
	int total = 0;
	for (int x0 = 0; x0 < 8 ; x0++) {
		for (int x1 = 0; x1 < 8 ; x1++) {
			if (x1 == x0)
				continue;
			total += tab[x0][x1];
			for (int x2 = 0; x2 < 8 ; x2++) {
				if (x2 == x1 || x2 == x0)
					continue;
				total += tab[x1][x2];
				for (int x3 = 0; x3 < 8; x3++) {
					if (x3 == x2 || x3 == x1 || x3 == x0)
						continue;
					total += tab[x2][x3];
					for (int x4 = 0; x4 < 8; x4++) {
						if (x4 == x3 || x4 == x2 || x4 == x1 || x4 == x0)
							continue;
						total += tab[x3][x4];
						for (int x5 = 0; x5 < 8; x5++) {
							if (x5 == x4 || x5 == x3 || x5 == x2 || x5 == x1 || x5 == x0)
								continue;
							total += tab[x4][x5];
							for (int x6 = 0; x6 < 8; x6++) {
								if (x6 == x5 || x6 == x4 || x6 == x3 || x6 == x2 || x6 == x1 || x6 == x0)
									continue;
								total += tab[x5][x6];
								for (int x7 = 0; x7 < 8; x7++) {
									if (x7 == x6 || x7 == x5 || x7 == x4 || x7 == x3 || x7 == x2 || x7 == x1 || x7 == x0)
										continue;
									total += tab[x6][x7];
									if (total < shortest)
										shortest = total;
									total -= tab[x6][x7];
								}
								total -= tab[x5][x6];
							}
							total -= tab[x4][x5];
						}
						total -= tab[x3][x4];
					}
					total -= tab[x2][x3];
				}
				total -= tab[x1][x2];
			}
			total -= tab[x0][x1];
		}
	}
	printf("%d\n", shortest);
}
