#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <iostream>
#include <string>
#include <set>
#include <deque>
#include <algorithm>
struct state {
	uint16_t a, b, c, d;
	uint8_t ra, rb, rc, rd;
	auto operator<=>(const state &) const & = default;
};
int solver(int aa, int ba, int ca, int cb, int da, int dc, int limit)
{
	int maxa = std::max({ba, ca, da});
	int time = 0;
	int maxg = 0;
	std::set<state> next_states;
	next_states.emplace(0, 0, 0, 0, 1, 0, 0, 0);
	while (next_states.size()) {
		std::deque<state> q;
		q.insert(q.end(), next_states.begin(), next_states.end());
		next_states.clear();
		time += 1;
		while (q.size()) {
			state s = q.back();
			q.pop_back();
			if (s.ra == maxa && s.a >= maxa)
				s.a = maxa;
			if (s.rb == cb && s.b >= cb)
				s.b = cb;
			if (s.rc == dc && s.c >= dc)
				s.c = dc;
			if (s.d + s.rd > maxg)
				maxg = s.d + s.rd;
			if (time < limit) {
				if (s.ra < maxa && s.a >= aa)
					next_states.emplace(s.a - aa + s.ra, s.b + s.rb,      s.c + s.rc,      s.d + s.rd, s.ra+1, s.rb,  s.rc,   s.rd);
				if (s.rb < cb && s.a >= ba)
					next_states.emplace(s.a - ba + s.ra, s.b + s.rb,      s.c + s.rc,      s.d + s.rd, s.ra,  s.rb+1, s.rc,   s.rd);
				if (s.rc < dc && s.a >= ca && s.b >= cb)
					next_states.emplace(s.a - ca + s.ra, s.b - cb + s.rb, s.c + s.rc,      s.d + s.rd, s.ra,  s.rb,   s.rc+1, s.rd);
				if (s.a >= da && s.c >= dc)
					next_states.emplace(s.a - da + s.ra, s.b + s.rb,      s.c - dc + s.rc, s.d + s.rd, s.ra,  s.rb,   s.rc,   s.rd+1);
				next_states.emplace(s.a + s.ra, s.b + s.rb, s.c + s.rc, s.d + s.rd, s.ra, s.rb, s.rc, s.rd);
			}
		}
	}
	return maxg;
}
int main()
{
	std::string s;
	int res1 = 0;
	int res2 = 1;
	while (std::getline(std::cin, s)) {
		int id, aa, ba, ca, cb, da, dc;
		int res = sscanf(s.c_str(),
				"Blueprint %d:"
				" Each ore robot costs %d ore."
				" Each clay robot costs %d ore."
				" Each obsidian robot costs %d ore and %d clay."
				" Each geode robot costs %d ore and %d obsidian.",
				&id, &aa, &ba, &ca, &cb, &da, &dc);
		assert(res == 7);
		res1 += id*solver(aa, ba, ca, cb, da, dc, 24);
		if (id <= 3)
			res2 *= solver(aa, ba, ca, cb, da, dc, 32);
	}
	std::cout << res1 << '\n' << res2 << '\n';
}
