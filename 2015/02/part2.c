#include <stdio.h>

int main()
{
	int l, w, h;
	int total = 0;
	while (3 == scanf("%dx%dx%d", &l, &w, &h)) {
		if (l > w) {
			l ^= w; w ^= l; l ^= w;
		}
		if (l > h) {
			l ^= h; h ^= l; l ^= h;
		}
		if (w > h) {
			w ^= h; h ^= w; w ^= h;
		}
		total += 2*(l+w) + l*w*h;
	}
	printf("%d\n", total);
}
