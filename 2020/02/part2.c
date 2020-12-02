#include <stdio.h>
#include <string.h>

int main()
{
	int valid = 0;
	char buf[512];
	int first, second;
	char c;
	while (4 == scanf(" %d-%d %c: %511s", &first, &second, &c, buf)) {
		first--;
		second--;
		int len = strlen(buf);
		if ((first < len && buf[first] == c) != (second < len && buf[second] == c))
			valid++;
	}
	printf("%d\n", valid);
}
