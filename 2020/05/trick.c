#include <stdio.h>

int main()
{
	char buf[512];
	char seats[128*8] = {0};
	while (1 == scanf("%511s", buf)) {
		int id = 0;
		for (int i = 0; i < 10; i++)
			id = id<<1 | ((buf[i]>>2^1)&1);
		seats[id] = 1;
	}
	for (int i = 128*8-1; i >= 0; i--)
		if (seats[i]) {
			printf("%d\n", i);
			break;
		}
	for (int i = 1; i < 128*8-1; i++)
		if (seats[i-1] && !seats[i] && seats[i+1]) {
			printf("%d\n", i);
			break;
		}
}
