#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
int check_year(char *p, int min, int max)
{
	if (isdigit(p[4]) && isdigit(p[5]) && isdigit(p[6]) && isdigit(p[7]) && !p[8]) {
		int year = atoi(&p[4]);
		return year >= min && year <= max;
	}
	return 0;
}
int check_height(char *p)
{
	int min = -1, max = -1;
	if (isdigit(p[4]) && isdigit(p[5])) {
		if (p[6] == 'i' && p[7] == 'n' && !p[8]) {
			min = 59;
			max = 76;
		} else if (isdigit(p[6]) && p[7] == 'c' && p[8] == 'm' && !p[9]) {
			min = 150;
			max = 193;
		}
	}
	if (min != -1) {
		int height = atoi(&p[4]);
		return height >= min && height <= max;
	}
	return 0;
}
int check_hcl(char *p)
{
	return p[4] == '#' && isxdigit(p[5]) && isxdigit(p[6]) && isxdigit(p[7])
		&& isxdigit(p[8]) && isxdigit(p[9]) && isxdigit(p[10]) && !p[11];
}
int check_ecl(char *p)
{
	return !memcmp(&p[4], "amb", 4) || !memcmp(&p[4], "blu", 4) || !memcmp(&p[4], "brn", 4)
		|| !memcmp(&p[4], "gry", 4) || !memcmp(&p[4], "grn", 4) || !memcmp(&p[4], "hzl", 4)
		|| !memcmp(&p[4], "oth", 4);
}
int check_pid(char *p)
{
	return isdigit(p[4]) && isdigit(p[5]) && isdigit(p[6]) && isdigit(p[7])
		&& isdigit(p[8]) && isdigit(p[9]) && isdigit(p[10]) && isdigit(p[11])
		&& isdigit(p[12]) && !p[13];
}
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
		if (!memcmp(buf, "byr:", 4) && check_year(buf, 1920, 2002))
			byr++;
		if (!memcmp(buf, "iyr:", 4) && check_year(buf, 2010, 2020))
			iyr++;
		if (!memcmp(buf, "eyr:", 4) && check_year(buf, 2020, 2030))
			eyr++;
		if (!memcmp(buf, "hgt:", 4) && check_height(buf))
			hgt++;
		if (!memcmp(buf, "hcl:", 4) && check_hcl(buf))
			hcl++;
		if (!memcmp(buf, "ecl:", 4) && check_ecl(buf))
			ecl++;
		if (!memcmp(buf, "pid:", 4) && check_pid(buf))
			pid++;
		if (!memcmp(buf, "cid:", 4))
			cid++;
	}
	if (byr && iyr && eyr && hgt && hcl && ecl && pid)
		total++;
	byr = iyr = eyr = hgt = hcl = ecl = pid = cid = 0;
	printf("%d\n", total);
}
