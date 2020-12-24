#include <stdio.h>
#define N 9
#define M 1000000
#define K 10000000
int input[N] = {
	3,9,4,6,1,8,5,2,7
};
int ls[M];
#define next(x) (ls[(x)])
int main() {
	for (int i = 0; i < N-1; i++)
		next(input[i]-1) = input[i+1]-1;
	next(input[N-1]-1) = N;
	for (int i = N; i < M; i++)
		next(i) = i+1;
	next(M-1) = input[0]-1;
	int idx = input[0]-1;
	for (int iter = 0; iter < K; iter++) {
		int a1 = next(idx);
		int a2 = next(a1);
		int a3 = next(a2);
		next(idx) = next(a3);
		int d = idx;
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
		next(a3) = next(d);
		next(d) = a1;
		idx = next(idx);
	}
	printf("%lld\n", (next(0)+1ll) * (next(next(0))+1ll));
}
