#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXSUBBAGS 4
#define MAXBAGS (18*33)
#define SHINY (14*33+11) /* shiny gold */
struct subbag {
	int count;
	int type;
};

enum {
	CANT_HOLD = 0,
	HOLDS_SHINY = 1,
	UNDECIDED = 2,
};
struct bag {
	struct subbag subbags[MAXSUBBAGS];
	int count;
	int state;
};

struct bag bags[MAXBAGS] = {0};

int parse(const char *p, const char *q);
int main()
{
	char buf1[64], buf2[64], c;

	while (2 == scanf("%63s%63s bags contain ", buf1, buf2)) {
		struct bag *bag = &bags[parse(buf1, buf2)];
		if (1 == scanf("no other bags%c", &c))
			continue;
		bag->state = UNDECIDED;
		for (int i = 0; i < MAXSUBBAGS; i++) {
			int count;
			scanf("%d%63s%63s bag", &count, buf1, buf2);
			bag->subbags[i].count = count;
			bag->subbags[i].type = parse(buf1, buf2);
			bag->count++;
			scanf(count>1?"s%c":"%c", &c);
			if (c == '.')
				break;
		}
	}
	bags[SHINY].state = HOLDS_SHINY;
	int left;
	do {
		left = 0;
		for (int i = 0; i < MAXBAGS; i++) {
			if (bags[i].state != UNDECIDED)
				continue;
			struct bag *bag = &bags[i];
			int undecided = 0;
			int j;
			for (j = 0; j < bag->count; j++) {
				int subtype = bag->subbags[j].type;
				if (bags[subtype].state == HOLDS_SHINY) {
					bag->state = HOLDS_SHINY;
					break;
				}
				if (bags[subtype].state == UNDECIDED)
					undecided = 1;
			}
			if (j == bag->count && !undecided)
				bag->state = CANT_HOLD;
			else
				left++;
		}
		printf("%d bags left\n", left);
	} while(left);
	int total = -1; /* exclude the shiny bag itself */
	for (int i = 0; i < MAXBAGS; i++)
		if (bags[i].state == HOLDS_SHINY)
			total++;
	printf("%d\n", total);
}


int parse1(const char *p)
{
	if (!strcmp(p, "bright"))
		return 0;
	if (!strcmp(p, "clear"))
		return 1;
	if (!strcmp(p, "dark"))
		return 2;
	if (!strcmp(p, "dim"))
		return 3;
	if (!strcmp(p, "dotted"))
		return 4;
	if (!strcmp(p, "drab"))
		return 5;
	if (!strcmp(p, "dull"))
		return 6;
	if (!strcmp(p, "faded"))
		return 7;
	if (!strcmp(p, "light"))
		return 8;
	if (!strcmp(p, "mirrored"))
		return 9;
	if (!strcmp(p, "muted"))
		return 10;
	if (!strcmp(p, "pale"))
		return 11;
	if (!strcmp(p, "plaid"))
		return 12;
	if (!strcmp(p, "posh"))
		return 13;
	if (!strcmp(p, "shiny"))
		return 14;
	if (!strcmp(p, "striped"))
		return 15;
	if (!strcmp(p, "vibrant"))
		return 16;
	if (!strcmp(p, "wavy"))
		return 17;
	printf("what's a %s?\n", p);
	abort();
}
int parse2(const char *p)
{
	if (!strcmp(p, "aqua"))
		return 0;
	if (!strcmp(p, "beige"))
		return 1;
	if (!strcmp(p, "black"))
		return 2;
	if (!strcmp(p, "blue"))
		return 3;
	if (!strcmp(p, "bronze"))
		return 4;
	if (!strcmp(p, "brown"))
		return 5;
	if (!strcmp(p, "chartreuse"))
		return 6;
	if (!strcmp(p, "coral"))
		return 7;
	if (!strcmp(p, "crimson"))
		return 8;
	if (!strcmp(p, "cyan"))
		return 9;
	if (!strcmp(p, "fuchsia"))
		return 10;
	if (!strcmp(p, "gold"))
		return 11;
	if (!strcmp(p, "gray"))
		return 12;
	if (!strcmp(p, "green"))
		return 13;
	if (!strcmp(p, "indigo"))
		return 14;
	if (!strcmp(p, "lavender"))
		return 15;
	if (!strcmp(p, "lime"))
		return 16;
	if (!strcmp(p, "magenta"))
		return 17;
	if (!strcmp(p, "maroon"))
		return 18;
	if (!strcmp(p, "olive"))
		return 19;
	if (!strcmp(p, "orange"))
		return 20;
	if (!strcmp(p, "plum"))
		return 21;
	if (!strcmp(p, "purple"))
		return 22;
	if (!strcmp(p, "red"))
		return 23;
	if (!strcmp(p, "salmon"))
		return 24;
	if (!strcmp(p, "silver"))
		return 25;
	if (!strcmp(p, "tan"))
		return 26;
	if (!strcmp(p, "teal"))
		return 27;
	if (!strcmp(p, "tomato"))
		return 28;
	if (!strcmp(p, "turquoise"))
		return 29;
	if (!strcmp(p, "violet"))
		return 30;
	if (!strcmp(p, "white"))
		return 31;
	if (!strcmp(p, "yellow"))
		return 32;
	printf("what's a %s?\n", p);
	abort();
}
int parse(const char *p, const char *q)
{
	/* 18 patterns */
	/* 33 colors */
	return parse1(p)*33 + parse2(q);
}
