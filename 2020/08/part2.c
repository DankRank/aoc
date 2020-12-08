#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum {
	NOP, ACC, JMP
};
struct insn {
	int op, arg, visited;
};
struct insn insns[700] = {0};
int main()
{
	char buf[512];
	int num;
	int n = 0;
	while (2 == scanf("%511s%d", buf, &num)) {
		if (!strcmp(buf, "nop"))
			insns[n].op = NOP;
		else if (!strcmp(buf, "acc"))
			insns[n].op = ACC;
		else if (!strcmp(buf, "jmp"))
			insns[n].op = JMP;
		else
			abort();
		insns[n].arg = num;
		n++;
	}

	int acc = 0;
	for (int i = 0; i < n ; i++) {
		if (insns[i].op != JMP)
			continue;
		insns[i].op = NOP;
		for (int j = 0; j < n; j++)
			insns[j].visited = 0;
		acc = 0;
		struct insn *ip = insns;
		while (!ip->visited) {
			if (ip - insns == n)
				goto foundit;
			ip->visited = 1;
			if (ip->op == ACC)
				acc += ip->arg;
			if (ip->op == JMP)
				ip += ip->arg;
			else
				ip++;
		}
		insns[i].op = JMP;
	}
foundit:
	printf("%d\n", acc);
}
