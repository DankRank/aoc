#include <stdio.h>

#define DH_G 7
#define DH_P 20201227
unsigned modpow(unsigned base, unsigned exp)
{
	unsigned long long x = base % DH_P;
	unsigned long long y = 1;

	while (exp) {
		if (exp&1)
			y = y*x % DH_P;
		exp >>= 1;
		x = x*x % DH_P;
	}
	return y;
}

unsigned crack_dh(unsigned target)
{
	unsigned exp = 0;
	unsigned long long x = 1;
	while (x != target) {
		x = x*DH_G % DH_P;
		exp++;
	}
	return exp;
}


int main()
{
	unsigned pa = 12320657;
	unsigned pb = 9659666;
	unsigned sb = crack_dh(pb);
	unsigned s = modpow(pa, sb);
	printf("%u\n", s);
}

