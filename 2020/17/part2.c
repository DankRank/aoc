#include <stdio.h>
#include <string.h>
#define PITCH_W (32*32*32)
#define PITCH_Z (32*32)
#define PITCH_Y (32)
#define PITCH_X (1)
char grid1[32][32][32][32] = {0};
char grid2[32][32][32][32] = {0};
char (*grid)[32][32][32] = grid1;
char (*offgrid)[32][32][32] = grid2;
static inline int neighbors(char *p)
{
	int n = 0;
	for (int i = -PITCH_W; i <= PITCH_W; i += PITCH_W)
		for (int j = -PITCH_Z; j <= PITCH_Z; j += PITCH_Z)
			for (int k = -PITCH_Y; k <= PITCH_Y; k += PITCH_Y)
				for (int l = -PITCH_X; l <= PITCH_X; l += PITCH_X)
					if ((i || j || k || l) && *(p+i+j+k+l))
						n++;
	return n;
}
int advance()
{
	int dirty = 0;
	for (int i = 1; i < 31; i++)
		for (int j = 1; j < 31; j++)
			for (int k = 1; k < 31; k++)
				for (int l = 1; l < 31; l++) {
					int n = neighbors(&grid[i][j][k][l]);
					char newcell;
					if (n == 3 || (n == 2 && grid[i][j][k][l]))
						newcell = 1;
					else
						newcell = 0;
					if (newcell != grid[i][j][k][l])
						dirty = 1;
					offgrid[i][j][k][l] = newcell;
				}
	char (*tmp)[32][32][32] = grid;
	grid = offgrid;
	offgrid = tmp;
	return dirty;
}
int count()
{
	int total = 0;
	for (int i = 1; i < 31; i++)
		for (int j = 1; j < 31; j++)
			for (int k = 1; k < 31; k++)
				for (int l = 1; l < 31; l++)
				total += grid[i][j][k][l];
	return total;
}
int main()
{
	char buf[512];
	char *s = &grid1[16][10][10][10];
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
