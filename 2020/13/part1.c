#include <stdio.h>

int main()
{
	int timestart;
	scanf("%d ", &timestart);
	int set[100];
	int n = 0;
	for (;;) {
		if (1 != scanf("%d,", &set[n])) {
			int test = 0;
			scanf("x%n,",&test);
			if (test != 1)
				break;
		} else {
			n++;
		}
	}
	for (int i = timestart; ; i++) {
		for (int j = 0; j < n; j++ ) {
			if(i%set[j] == 0) {
				printf("%d\n",(i-timestart) * set[j]);
				return 0;
			}
		}
	}
}
