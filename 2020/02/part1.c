#include <stdio.h>

int main()
{
	int valid = 0;
	char buf[512];
	int min, max;
	char c;
	while (4 == scanf("%d-%d %c: %511s", &min, &max, &c, buf)) {
		int count = 0;
		char *p = buf;
		while (*p)
			if (*p++ == c)
				count++;
		if (count >= min && count <= max)
			valid++;
	}
	printf("%d\n", valid);
}
