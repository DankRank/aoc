#include <stdio.h>

int main()
{
	char buf[512];
	int total = 0;
	while (1 == scanf("%511s", buf)) {
		char *p = buf;
		while (*p) {
			if (p[0] == '\\') {
				if (p[1] == 'x') {
					p += 4;
					total += 3;
				} else {
					p += 2;
					total++;
				}
			} else {
				if (p[0] == '"')
					total++;
				p++;
			}
		}
	}
	printf("%d\n", total);
}
