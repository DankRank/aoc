#include <stdio.h>
#include <string.h>
/* decided to do this with matricies, for fun */
const int matrix_left[] = { 0, 1, -1, 0 };
const int matrix_right[] = { 0, -1, 1, 0 };
static inline void mv_mul(const int lhs[2*2], int rhs[2])
{
	int x = lhs[0]*rhs[0] + lhs[2]*rhs[1];
	int y = lhs[1]*rhs[0] + lhs[3]*rhs[1];
	rhs[0] = x;
	rhs[1] = y;
}
static inline void vvs_fma(int lhs[2], const int rhs[2], int a)
{
	lhs[0] += rhs[0]*a;
	lhs[1] += rhs[1]*a;
}
#define abs(x) ((x)<0?-(x):(x))
int main()
{
	int pos[2] = {0,0};
	int forward[2] = {10,1};

	char c;
	int a;
	while (2 == scanf(" %c%d", &c, &a)) {
		switch (c) {
		case 'N': forward[1] += a; break;
		case 'S': forward[1] -= a; break;
		case 'E': forward[0] += a; break;
		case 'W': forward[0] -= a; break;
		case 'L':
			for (int i = 0; i < a/90; i++)
				mv_mul(matrix_left, forward);
			break;
		case 'R':
			for (int i = 0; i < a/90; i++)
				mv_mul(matrix_right, forward);
			break;
		case 'F':
			vvs_fma(pos, forward, a);
			break;
		}
	}
	printf("%d\n", abs(pos[0])+abs(pos[1]));
}
