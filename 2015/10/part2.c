#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 50
int main()
{
	char *buf1 = malloc(512), *buf2;
	if (!buf1)
		abort();
	scanf("%511s", buf1);
	buf2 = malloc(strlen(buf1)*2+1);
	if (!buf2)
		abort();
	for (int i = 0; i < N; i++) {
		int dig = buf1[0];
		int count = 0;
		char *p = buf1, *q = buf2;
		while (*p) {
			if (*p != dig) {
				if (count > 9)
					abort();
				*q++ = count + '0';
				*q++ = dig;
				dig = *p;
				count = 0;
			}
			p++;
			count++;
		}
		if (count > 9)
			abort();
		*q++ = count + '0';
		*q++ = dig;
		*q++ = '\0';

		p = buf1;
		buf1 = buf2;
		buf2 = p;
		buf2 = realloc(buf2, strlen(buf1)*2+1);
		if (!buf2)
			abort();
	}
	int len = strlen(buf1);
	printf("%d\n", len);
	free(buf1);
	free(buf2);
}
