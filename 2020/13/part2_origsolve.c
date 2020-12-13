#include <stdio.h>
#include <assert.h>

int main()
{
	/* 431x + 31 = 409y
	 * wolfram solved this as
	 * x = 409n+389, y = 431n+410
	 *
	 * 176279n+167659 + 31 = 409y
	 *
	 * subtract 23 from the starting constant
	 * 167636
	 */
	for (long i = 167636; ; i += 176279) {
		if ((i+64)%41 == 0 &&
			(i+17)%37 == 0 &&
			(i+83)%29 == 0 &&
			(i+0)%23 == 0 &&
			(i+42)%19 == 0 &&
			(i+37)%17 == 0 &&
			(i+36)%13 == 0) {
			printf("%ld\n", i);
			return 0;
		}
	}
}
