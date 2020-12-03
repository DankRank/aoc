#include <stdio.h>
#include <string.h>

char grid[1000][1000] = {0};
int main()
{
	char cmd[10];
	int total = 0;
	while (1 == scanf("%9s", cmd)) {
		int turn = !strcmp(cmd, "turn");
		int arg = 0;
		if (turn) {
			scanf("%9s", cmd);
			arg = !strcmp(cmd, "on");
		}

		int x1,y1,x2,y2;
		scanf("%d,%d through %d,%d",&x1,&y1,&x2,&y2);
		if (x1 > x2) {
			x1 ^= x2; x2 ^= x1; x1 ^= x2;
		}
		if (y1 > y2) {
			y1 ^= y2; y2 ^= y1; y1 ^= y2;
		}
		for (int i = y1; i <= y2; i++)
			for (int j = x1; j <= x2; j++)
				if (turn) {
					grid[i][j] += arg*2 - 1;
					if (grid[i][j] < 0)
						grid[i][j] = 0;
					else
						total += arg*2 - 1;
				} else {
					total += 2;
					grid[i][j] += 2;
				}
	}
	printf("%d\n", total);
}
