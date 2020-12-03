#include <stdio.h>
#include <stdlib.h>
#include <string.h>
enum {
	UNDEFINED = 0,
	NOT = 1,
	AND = 2,
	OR = 3,
	LSHIFT = 4,
	RSHIFT = 5,
	COPY = 6,
	INSMASK = 7,
	OP1CONST = 128,
	OP2CONST = 64,
	POPULATED = 32
};
struct cell {
	char opcode;
	unsigned short op1;
	unsigned short op2;
	unsigned short value;
};
struct cell cells[26*26 + 26] = {{0}};

short regindex(char *p)
{
	if (!p[0])
		abort();
	if (!p[1])
		return p[0]-'a';
	return 26*(p[0]-'a'+1) + p[1]-'a';
}
const char *regname(short r) {
	static char buf[3] = {0};
	if (r < 26) {
		buf[0] = r+'a';
		buf[1] = 0;
	} else {
		buf[0] = r/26-1+'a';
		buf[1] = r%26 + 'a';
		buf[2] = 0;
	}
	return buf;
}

enum {
	T_RARROW,
	T_OP,
	T_REG,
	T_CONST,
	T_EOF,
};

int scan_raw(unsigned short *p)
{
	static char buf[512];
	if (1 != scanf("%511s", buf))
		return T_EOF;
	if (!strcmp(buf, "->"))
		return T_RARROW;
	if (!strcmp(buf, "NOT"))
		return *p=NOT, T_OP;
	if (!strcmp(buf, "AND"))
		return *p=AND, T_OP;
	if (!strcmp(buf, "OR"))
		return *p=OR, T_OP;
	if (!strcmp(buf, "LSHIFT"))
		return *p=LSHIFT, T_OP;
	if (!strcmp(buf, "RSHIFT"))
		return *p=RSHIFT, T_OP;
	if (buf[0] >= 'a' && buf[0] <= 'z')
		return *p=regindex(buf), T_REG;
	if (buf[0] >= '0' && buf[0] <= '9')
		return sscanf(buf, "%hu", p), T_CONST;
	return T_EOF;
}
int scan(unsigned short *a)
{
	int tok = scan_raw(a);
#if 0
	switch (tok) {
	case T_RARROW: printf("->\n"); break;
	case T_OP: printf("OP(%d)\n", *a); break;
	case T_REG: printf("%s\n",regname(*a)); break;
	case T_CONST: printf("%d\n",*a); break;
	case T_EOF: printf("EOF\n"); break;
	}
#endif
	return tok;
}
/* lines ::= lines line | line
 * line ::= op arg -> reg | arg op arg -> reg | arg -> reg
 * arg ::= reg | const
 */
void parse()
{
	for ( ;;) {
		int tok;
		unsigned short a;
		char opcode = 0;
		unsigned short op1 = 0;
		unsigned short op2 = 0;
		tok = scan(&a);
		if (tok == T_EOF)
			break;
		if (tok == T_OP) { /* unary */
			opcode |= a;
			tok = scan(&a);
			if (tok == T_CONST)
				opcode |= OP1CONST;
			op1 = a;
			opcode |= OP2CONST;
			scan(&a); /* rarrow */
		} else { /* binary */
			if (tok == T_CONST)
				opcode |= OP1CONST;
			op1 = a;
			tok = scan(&a);
			if (tok == T_RARROW) {
				opcode |= COPY | OP2CONST;
			} else {
				opcode |= a;
				tok = scan(&a);
				if (tok == T_CONST)
					opcode |= OP2CONST;
				op2 = a;
				scan(&a); /* rarrow */
			}
		}
		scan(&a); /* reg */
		cells[a].opcode = opcode;
		cells[a].op1 = op1;
		cells[a].op2 = op2;
		cells[a].value = 0;
	}
}

int main()
{
	parse();

	unsigned short stack[350] = {0};
	int sp = 0;
	for (;;) {
		unsigned short cur = stack[sp];
		char opcode = cells[cur].opcode;
		unsigned short op1 = cells[cur].op1;
		unsigned short op2 = cells[cur].op2;
		if (!(opcode & OP1CONST)) {
			if (cells[op1].opcode & POPULATED) {
				cells[cur].op1 = cells[op1].value;
				cells[cur].opcode |= OP1CONST;
			} else {
				stack[++sp] = op1;
				continue;
			}
		}
		if (!(opcode & OP2CONST)) {
			if (cells[op2].opcode & POPULATED) {
				cells[cur].op2 = cells[op2].value;
				cells[cur].opcode |= OP2CONST;
			} else {
				stack[++sp] = op2;
				continue;
			}
		}

		op1 = cells[cur].op1;
		op2 = cells[cur].op2;
		switch (opcode & INSMASK) {
			case NOT:
				cells[cur].value = ~op1;
				break;
			case AND:
				cells[cur].value = op1 & op2;
				break;
			case OR:
				cells[cur].value = op1 | op2;
				break;
			case LSHIFT:
				cells[cur].value = op1 << op2;
				break;
			case RSHIFT:
				cells[cur].value = op1 >> op2;
				break;
			case COPY:
				cells[cur].value = op1;
				break;
		}
		cells[cur].opcode |= POPULATED;
		if (sp == 0)
			break;
		sp--;
	}
	printf("%d\n", cells[0].value);
}
