#include <stdio.h>
#include <stdlib.h>
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
	int myt[30];
	int t[300][30];
	int nf = 0;
	int nt = 0;
	int m[30][30] = {0};
	char buf[512];
	while (fgets(buf, 512, stdin)) {
		if (buf[0] == '\n')
			break;
		sscanf(strchr(buf, ':'), ": %d-%d or %d-%d", &f[nf].lo1, &f[nf].hi1, &f[nf].lo2, &f[nf].hi2);
		nf++;
	}
	fgets(buf, 512, stdin); /* your ticket: */
	fgets(buf, 512, stdin);
	read_numbers(buf, myt);
	fgets(buf, 512, stdin); /* empty line */
	fgets(buf, 512, stdin); /* nearby tickets: */
	while (fgets(buf, 512, stdin)) {
		if (buf[0] == '\n')
			break;
		read_numbers(buf, t[nt]);
		nt++;
	}
	for (int k = 0; k < nt; k++)
		for (int i = 0; i < nf; i++) {
			for (int j = 0; j < nf; j++)
				if ((f[j].lo1 <= t[k][i] && t[k][i] <= f[j].hi1) || (f[j].lo2 <= t[k][i] && t[k][i] <= f[j].hi2))
					goto valid;
			memmove(&t[k], &t[k+1], (nt-k-1)*sizeof(t[k]));
			nt--;
			k--;
		valid:;
		}
	for (int i = 0; i < nf; i++)
		for (int j = 0; j < nf; j++) {
			for (int k = 0; k < nt; k++)
				if (!((f[i].lo1 <= t[k][j] && t[k][j] <= f[i].hi1) || (f[i].lo2 <= t[k][j] && t[k][j] <= f[i].hi2)))
					goto invalid;
			m[i][j] = 1;
		invalid:;
		}
	int tab[30];
	for (int i = 0; i < nf; i++)
		tab[i] = -1;
	int left = 0;
	int lastleft = 0;
	do {
		lastleft = left;
		left = 0;
		for (int i = 0; i < nf; i++) {
			if (tab[i] != -1)
				continue;
			int first = -1;
			for (int j = 0; j < nf; j++)
				if (m[i][j]) {
					if (first == -1) {
						first = j;
					} else {
						left++;
						goto ambig;
					}
				}
			if (first == -1)
				abort();
			tab[i] = first;
			for (int k = 0; k < nf; k++) {
				if (tab[k] != -1)
					continue;
				m[k][first] = 0;
			}
		ambig:;
		}
		printf("left: %d\n", left);
	} while (left && left != lastleft);
	for (int i = 0; i < nf; i++) {
		printf("%2d:", i);
		for (int j = 0; j < nf; j++) {
			printf(" %d", m[i][j]);
		}
		printf(" (%2d)\n", tab[i]);
	}
	if (left)
		abort();
	long total = 1;
	for (int i = 0; i < 6; i++)
		total *= myt[tab[i]];
	printf("%ld\n", total);
}
