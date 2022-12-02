%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int yylex(void);
#define yyerror(s) ((void)fprintf(stderr, "%s\n", s))
struct point {
	int x, y;
	//      (0,1) (1,1)
	// (-1, 0) (0, 0) (1, 0)
	//     (-1,-1) (0,-1)
};
void flip(struct point pt);
%}

%union {
	struct point pt;
}

%type <pt> list
%%
start:
	%empty
	| start list '\n' { flip($2); }
list:
	%empty { $$.x = 0; $$.y = 0; }
	| list 'w' { $$.x--; }
	| list 'e' { $$.x++; }
	| list 'n' 'w' { $$.y++; }
	| list 'n' 'e' { $$.x++; $$.y++; }
	| list 's' 'w' { $$.x--; $$.y--; }
	| list 's' 'e' { $$.y--; }
	;

%%
struct point ls1[5000], ls2[5000];
int ls_len = 0;

struct point *ls = ls1;
struct point *ls_back = ls2;
int compare(const struct point *lhs, const struct point *rhs)
{
	if (lhs->x == rhs->x)
		return lhs->y - rhs->y;
	else
		return lhs->x - rhs->x;
}
int search(struct point pt)
{
	int left = 0;
	int right = ls_len;
	while (left < right) {
		int mid = (left+right)/2;
		if (compare(&ls[mid], &pt) < 0)
			left = mid + 1;
		else
			right = mid;
	}
	return left;
}
int contains(struct point pt)
{
	int idx = search(pt);
	return idx != ls_len && ls[idx].x == pt.x && ls[idx].y == pt.y;
}
void flip(struct point pt)
{
	int idx = search(pt);
	if (idx == ls_len || ls[idx].x != pt.x || ls[idx].y != pt.y) {
		memmove(&ls[idx+1], &ls[idx], (ls_len-idx)*sizeof(pt));
		ls[idx] = pt;
		ls_len++;
	} else {
		memmove(&ls[idx], &ls[idx+1], (ls_len-idx-1)*sizeof(pt));
		ls_len--;
	}
}
int yylex()
{
	int c = getchar();
	switch (c) {
	case 'n':
	case 's':
	case 'e':
	case 'w':
	case '\n':
		return c;
	case EOF:
		return YYEOF;
	}
	return YYUNDEF;
}

// garbage code

#define CHECKWHITE(xxx,yyy) do { \
	if ((x==-xxx && y==-yyy) ||contains((struct point){pt.x+x+xxx, pt.y+y+yyy})) \
		count++; \
} while(0)

int checkwhites(struct point pt, int x, int y)
{
	int count = 0;
	CHECKWHITE(1,0);
	CHECKWHITE(1,1);
	CHECKWHITE(0,1);
	CHECKWHITE(-1,0);
	CHECKWHITE(-1,-1);
	CHECKWHITE(0,-1);
	return count == 2;
}
int putunique(int len, struct point pt)
{
	for (int i = 0; i < len; i++) {
		if (ls_back[i].x == pt.x && ls_back[i].y == pt.y)
			return 0;
	}
	ls_back[len] = pt;
	return 1;
}
#define CHECK(xxx,yyy) do { \
	if (contains((struct point){pt.x+xxx, pt.y+yyy})) \
		count++; \
	else \
		if (checkwhites(pt, xxx, yyy)) \
			if (putunique(nlen, (struct point){pt.x+xxx, pt.y+yyy})) \
				nlen++; \
} while(0)
void step() {
	int nlen = 0;

	for (int i = 0; i < ls_len; i++) {
		struct point pt = ls[i];
		int count = 0;
		CHECK(1,0);
		CHECK(1,1);
		CHECK(0,1);
		CHECK(-1,0);
		CHECK(-1,-1);
		CHECK(0,-1);
		if (count == 1 || count == 2)
			ls_back[nlen++] = ls[i];
	}
	struct point *tmp = ls;
	ls = ls_back;
	ls_back = tmp;
	ls_len = nlen;
	qsort(ls, nlen, sizeof(struct point), (int(*)(const void*,const void*))compare);
}
int main()
{
	if (yyparse())
		return 1;
	for (int i = 0; i < 100; i++)
		step();
	printf("%d\n", ls_len);
}
