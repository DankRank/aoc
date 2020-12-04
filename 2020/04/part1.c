#include <stdio.h>
#include <string.h>

int main()
{
	int spaces;
	char buf[512];
	int total = 0;

	int byr = 0, iyr = 0, eyr = 0, hgt = 0, hcl = 0, ecl = 0, pid = 0, cid = 0;
	while (1 == scanf(" %n%511s", &spaces, buf)) {
		if (spaces == 2) {
			if (byr && iyr && eyr && hgt && hcl && ecl && pid)
				total++;
			byr = iyr = eyr = hgt = hcl = ecl = pid = cid = 0;
		}
		if (!memcmp(buf, "byr:", 4))
			byr++;
		if (!memcmp(buf, "iyr:", 4))
			iyr++;
		if (!memcmp(buf, "eyr:", 4))
			eyr++;
		if (!memcmp(buf, "hgt:", 4))
			hgt++;
		if (!memcmp(buf, "hcl:", 4))
			hcl++;
		if (!memcmp(buf, "ecl:", 4))
			ecl++;
		if (!memcmp(buf, "pid:", 4))
			pid++;
		if (!memcmp(buf, "cid:", 4))
			cid++;
	}
	if (byr && iyr && eyr && hgt && hcl && ecl && pid)
		total++;
	byr = iyr = eyr = hgt = hcl = ecl = pid = cid = 0;
	printf("%d\n", total);
}
