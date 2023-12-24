#include "md5.h"
#define MD5_DIGEST_LENGTH 16
static void MD5(unsigned char *data, unsigned long size, unsigned char *result)
{
	MD5_CTX ctx;
	MD5_Init(&ctx);
	MD5_Update(&ctx, data, size);
	MD5_Final(result, &ctx);
}
