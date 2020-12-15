#include <stdio.h>

int main()
{
	// dumb variable names sorry about that
	static int last[3000] = {0};
	int last2;
	int n = 1;
	int x;
	int lastx;
	while (1 == scanf("%d,", &x)) {
		last2 = last[x];
		last[x] = n++;
		lastx = x;
	}
	while (n != 2021) {
		if (!last2)
			x = 0;
		else
			x = n-1 - last2;

		last2 = last[x];
		last[x] = n++;
		lastx = x;
	}
	printf("%d\n", lastx);
}
