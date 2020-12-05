#include <stdio.h>

int main()
{
	char buf[512];
	char seats[128*8] = {0};
	while (1 == scanf("%511s", buf)) {
		int row = 0, col = 0;
		for (int i = 0; i < 7; i++)
			row = row<<1 | (buf[i] == 'B'); /* 'F' */
		for (int i = 0; i < 3; i++)
			col = col<<1 | (buf[7+i] == 'R'); /* 'L' */
		int id = row<<3 | col;
		seats[id] = 1;
	}
	for (int i = 128*8-1; i >= 0; i--)
		if (seats[i]) {
			printf("%d\n", i);
			return 0;
		}
}
