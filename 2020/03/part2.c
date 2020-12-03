#include <stdio.h>
#include <string.h>

int main()
{
	char buf[512] = {0};
	scanf("%511s", buf);
	int w = strlen(buf);
	int i = 0;
	int c1 = 0, c2 = 0, c3 = 0, c4 = 0, c5 = 0;
	int even = 0;
	while (1 == scanf("%511s", buf)) {
		i++;
		if (buf[i%w] == '#')
			c1++;
		if (buf[(i*3)%w] == '#')
			c2++;
		if (buf[(i*5)%w] == '#')
			c3++;
		if (buf[(i*7)%w] == '#')
			c4++;
		if (even && buf[(i/2)%w] == '#')
			c5++;
		even = !even;
	}
	printf("%u\n", 1u*c1*c2*c3*c4*c5);
}

