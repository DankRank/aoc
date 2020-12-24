%{
#include <stdio.h>
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
struct point ls[400];
int ls_len = 0;
int search(struct point pt)
{
	int left = 0;
	int right = ls_len;
	while (left < right) {
		int mid = (left+right)/2;
		if (pt.x > ls[mid].x || (pt.x == ls[mid].x && pt.y > ls[mid].y))
			left = mid + 1;
		else
			right = mid;
	}
	return left;
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
int main()
{
	if (!yyparse())
		printf("%d\n", ls_len);
}
