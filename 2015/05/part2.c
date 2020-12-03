#include <stdio.h>

int main()
{
	char buf[512];
	int total = 0;
	while (1 == scanf("%511s", buf)) {
		char *p = buf;
		int xyxy = 0;
		int wow = 0;
		while (*p) {
			if (p[1]) {
				if (p[0] == p[2])
					wow = 1;
				char *q = &p[2];
				while (*q) {
					if (p[0] == q[0] && p[1] == q[1])
						xyxy = 1;
					q++;
				}
			}
			p++;
		}
		if (xyxy && wow)
			total++;
	}
	printf("%d\n", total);
}
