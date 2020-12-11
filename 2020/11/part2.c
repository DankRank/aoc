#include <stdio.h>
#include <string.h>

char grid1[100][100];
char grid2[100][100];
int width;
int height;
char (*grid)[100] = grid1;
char (*offgrid)[100] = grid2;
#define RAY(dir) do { \
	char *q = &p[dir]; \
	while (*q == '.') \
		q = &q[dir]; \
	total += *q == '#'; \
} while(0)
static inline int neighbors(char *p)
{
	int total = 0;
	RAY(-101); RAY(-100); RAY(-99);
	RAY(-1); RAY(1);
	RAY(99); RAY(100); RAY(101);
	return total;
}
int advance()
{
	int dirty = 0;
	for (int i = 1; i <= height; i++)
		for (int j = 1; j <= width; j++)
			if (grid[i][j] != '.') {
				int n = neighbors(&grid[i][j]);
				char seat;
				if (n == 0)
					seat = '#';
				else if (n >= 5)
					seat = 'L';
				else
					seat = grid[i][j];
				if (seat != grid[i][j])
					dirty = 1;
				offgrid[i][j] = seat;
			}
	char (*tmp)[100] = grid;
	grid = offgrid;
	offgrid = tmp;
	return dirty;
}
int main()
{
	memset(grid1, 'L', sizeof(grid1));

	char buf[512];
	scanf("%511s",buf);
	width = strlen(buf);
	height = 0;
	memcpy(&grid1[++height][1], buf, width);
	while (1 == scanf("%511s", buf))
		memcpy(&grid1[++height][1], buf, width);
	memcpy(grid2, grid1, sizeof(grid1));

	while (advance())
		;
	int total = 0;
	for (int i = 1; i <= height; i++)
		for (int j = 1; j <= width; j++)
			total += grid[i][j] == '#';
	printf("%d\n", total);
}
