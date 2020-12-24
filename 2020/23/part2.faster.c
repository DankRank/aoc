#include <stdio.h>
#define N 9
#define M 1000000
int input[N] = {
	3,9,4,6,1,8,5,2,7
};
struct node {
	int val;
	int next;
} ls[M];
#define car(x) (ls[(x)].val)
#define cdr(x) (ls[(x)].next)
int main() {
	for (int i = 0; i < 9; i++) {
		car(i) = input[i]-1;
		cdr(i) = i+1;
	}
	for (int i = N; i < M; i++) {
		car(i) = i;
		cdr(i) = i+1;
	}
	cdr(M-1) = 0;
	int idx = 0;
	for (int iter = 0; iter < M; iter++) {
		if (!(iter & 1023))
			printf("%d\n", iter);
		int sub1 = cdr(idx);
		int sub2 = cdr(sub1);
		int sub3 = cdr(sub2);
		cdr(idx) = cdr(sub3);
		int a1 = car(sub1);
		int a2 = car(sub2);
		int a3 = car(sub3);
		int d = car(idx);
		d = d ? d-1 : M-1;
		if (d == a1 || d == a2 || d == a3) {
			d = d ? d-1 : M-1;
			if (d == a1 || d == a2 || d == a3) {
				d = d ? d-1 : M-1;
				if (d == a1 || d == a2 || d == a3) {
					d = d ? d-1 : M-1;
				}
			}
		}
		int dx = idx;
		while (car(dx) != d)
			dx = cdr(dx);
		cdr(sub3) = cdr(idx);
		cdr(idx) = sub1;
		idx = cdr(idx);
	}
	idx = 0;
	while (car(idx) != 0)
		idx = cdr(idx);
	printf("%lld\n", (car(cdr(idx))+1ll) * (car(cdr(cdr(idx)))+1ll));
}
