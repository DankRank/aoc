#include <stdio.h>
#include <string.h>
#define PITCH_Z (100*100)
#define PITCH_Y (100)
#define PITCH_X (1)
char grid1[100][100][100] = {0};
char grid2[100][100][100] = {0};
char (*grid)[100][100] = grid1;
char (*offgrid)[100][100] = grid2;
static inline int neighbors(char *p)
{
	int n = 0;
	for (int i = -PITCH_Z; i <= PITCH_Z; i += PITCH_Z)
		for (int j = -PITCH_Y; j <= PITCH_Y; j += PITCH_Y)
			for (int k = -PITCH_X; k <= PITCH_X; k += PITCH_X)
				if ((i || j || k) && *(p+i+j+k))
					n++;
	return n;
}
int advance()
{
	int dirty = 0;
	for (int i = 1; i < 99; i++)
		for (int j = 1; j < 99; j++)
			for (int k = 1; k < 99; k++) {
				int n = neighbors(&grid[i][j][k]);
				char newcell;
				if (n == 3 || (n == 2 && grid[i][j][k]))
					newcell = 1;
				else
					newcell = 0;
				if (newcell != grid[i][j][k])
					dirty = 1;
				offgrid[i][j][k] = newcell;
			}
	char (*tmp)[100][100] = grid;
	grid = offgrid;
	offgrid = tmp;
	return dirty;
}
int count()
{
	int total = 0;
	for (int i = 1; i < 99; i++)
		for (int j = 1; j < 99; j++)
			for (int k = 1; k < 99; k++)
				total += grid[i][j][k];
	return total;
}
int main()
{
	char buf[512];
	char *s = &grid1[50][50][50];
	while (1 == scanf("%511s", buf)) {
		for (char *p = s, *q = buf; *q; p++, q++)
			*p = *q == '#';
		s += PITCH_Y;
	}
	memcpy(grid2, grid1, sizeof(grid1));
	advance();
	advance();
	advance();
	advance();
	advance();
	advance();
	printf("%d\n", count());
}
