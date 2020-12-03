#include <stdio.h>

int main()
{
	char buf[512];
	int total = 0;
	while (1 == scanf("%511s", buf)) {
		char *p = buf;
		int vowels = 0;
		int twice = 0;
		while (*p) {
			if (p[0] == 'a' || p[0] == 'e' || p[0] == 'i' || p[0] == 'o' ||p[0] == 'u')
				vowels++;
			if (p[0] == p[1])
				twice = 1;
			if (p[0] == 'a' && p[1] == 'b')
				break;
			if (p[0] == 'c' && p[1] == 'd')
				break;
			if (p[0] == 'p' && p[1] == 'q')
				break;
			if (p[0] == 'x' && p[1] == 'y')
				break;
			p++;
		}
		if (vowels >= 3 && twice && !*p)
			total++;
	}
	printf("%d\n", total);
}
