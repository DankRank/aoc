#include <stdio.h>
#include <string.h>
#include "mymd5.h"
int main() {
	const char *key = "ckczppom";
	char buf[512];
	unsigned char digest[MD5_DIGEST_LENGTH];
	int i = 1;
	for (;;) {
		snprintf(buf, 512, "%s%d", key, i++);
		MD5((unsigned char*)buf, strlen(buf), digest);
		if (!digest[0] && !digest[1] && !digest[2]) {
			printf("%d\n", i-1);
			break;
		}
	}
}
