#include <stdio.h>

int main()
{
	char buf[512];
	int total = 0;
	while (1 == scanf("%511s", buf)) {
		char *p = buf;
		total += 2;
		while (*p) {
			if (*p == '\\' || *p == '"')
				total++;
			p++;
		}
	}
	printf("%d\n", total);
}
