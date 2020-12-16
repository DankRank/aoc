#include <stdio.h>
#include <string.h>
struct field {
	int lo1, hi1, lo2, hi2;
};
void read_numbers(const char *s, int arr[])
{
	for (int i = 0; ; i++) {
		int n = 0;
		sscanf(s, "%d,%n", &arr[i], &n);
		if (!n)
			break;
		s += n;

	}
}
int main()
{
	struct field f[30];
	int t[30];
	int nf = 0;
	char buf[512];
	while (fgets(buf, 512, stdin)) {
		if (buf[0] == '\n')
			break;
		sscanf(strchr(buf, ':'), ": %d-%d or %d-%d", &f[nf].lo1, &f[nf].hi1, &f[nf].lo2, &f[nf].hi2);
		nf++;
	}
	fgets(buf, 512, stdin); /* your ticket: */
	fgets(buf, 512, stdin);
	read_numbers(buf, t);
	fgets(buf, 512, stdin); /* empty line */
	fgets(buf, 512, stdin); /* nearby tickets: */
	int total = 0;
	while (fgets(buf, 512, stdin)) {
		read_numbers(buf, t);
		for (int i = 0; i < nf; i++) {
			for (int j = 0; j < nf; j++)
				if ((f[j].lo1 <= t[i] && t[i] <= f[j].hi1) || (f[j].lo2 <= t[i] && t[i] <= f[j].hi2))
					goto valid;
			total += t[i];
valid:;
		}
	}
	printf("%d\n", total);
}
