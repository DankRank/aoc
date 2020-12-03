#include <stdio.h>
#include <string.h>

int main()
{
	char buf[512] = {0};
	scanf("%511s", buf);
	int w = strlen(buf);
	int i = 0;
	int count = 0;
	while (1 == scanf("%511s", buf)) {
		i = (i+3) % w;
		if (buf[i] == '#')
			count++;
	}
	printf("%d\n", count);
}

