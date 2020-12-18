%{
#include <stdio.h>
#define yyerror(r, s) (fprintf(stderr, "%s\n", s))
int yylex(void);
%}
%define api.value.type {long}
%parse-param {long *result}
%token NUM
%%
Start:
	ExprList { *result = $1; }
ExprList:
	%empty { $$ = 0; }
	| ExprList Expr '\n' { $$ = $1 + $2; }
	;
PrimaryExpr:
	'(' Expr ')' { $$ = $2; }
	| NUM
	;
Expr:
	PrimaryExpr
	| Expr '*' PrimaryExpr { $$ = $1 * $3; }
	| Expr '+' PrimaryExpr { $$ = $1 + $3; }
	;
%%
int yylex()
{
	long v = 0;
	int c;
	do
		c = getc(stdin);
	while (c == ' ' || c == '\t');
	switch (c) {
		case '(':
		case ')':
		case '*':
		case '+':
		case '\n':
			return c;
		case EOF: return YYEOF;
	}
	if (c < '0' || c > '9')
		return YYUNDEF;
	while (c >= '0' && c <= '9') {
		v = v*10 + c-'0';
		c = getc(stdin);
	}
	ungetc(c, stdin);
	yylval = v;
	return NUM;
}
int main()
{
	long total;
	if (!yyparse(&total)) {
		printf("%ld\n", total);
	}
}
