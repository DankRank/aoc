#include <stdio.h>
#include <string.h>

int main()
{
	int spaces;
	char buf[512];
	int total = 0;

	char qs[26] = {0};
	int gcount = 0;
	while (1 == scanf(" %n%511s", &spaces, buf)) {
		if (spaces == 2) {
			for (int i = 0; i < 26; i++)
				total += qs[i] == gcount;
			memset(qs, 0, sizeof(qs));
			gcount = 0;
		}

		char *p = buf;
		while (*p)
			qs[*p++ - 'a']++;
		gcount++;
	}
	for (int i = 0; i < 26; i++)
		total += qs[i] == gcount;
	printf("%d\n", total);
}
