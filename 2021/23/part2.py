#!/usr/bin/env python3

A = 0
B = 1
C = 2
D = 3
cost_for_letter = [10**x for x in range(4)]

upperbound = 100000
known_states = {}
fini_state = None

class State:
    def __init__(self, hall, cols, cost):
        self.hall = hall
        self.cols = cols
        self.clean = [all(k == j for k in self.cols[j]) for j in range(4)]
        self.cost = cost
        self.hash = hash((self.hall, self.cols))

    def sethall(self, hall, val):
        return self.hall[:hall] + (val,) + self.hall[hall+1:]
    def popcol(self, col):
        return self.cols[:col] + (self.cols[col][1:],) + self.cols[col+1:]
    def pushcol(self, col, val):
        return self.cols[:col] + ((val,) + self.cols[col],) + self.cols[col+1:]

    def check(self):
        global upperbound
        if self in known_states and known_states[self].cost <= self.cost:
            return
        if self == fini_state and upperbound > self.cost:
            upperbound = self.cost
        known_states[self] = self
        self.moves()
    # 0 1   2   3   4   5 6
    #     0   1   2   3
    def moves(self):
        for i in range(7):
            j = self.hall[i]
            if j is not None and self.clean[j]:
                if all(self.hall[k] is None for k in (range(i+1, j+2) if i <= j+1 else range(j+2, i))):
                    ncost = self.cost + cost_for_letter[j]*self.dist(i, j)
                    if ncost > upperbound:
                        continue
                    State(self.sethall(i, None), self.pushcol(j, j), ncost).check()
        for j in range(4):
            if not self.clean[j]: # includes a len check
                val = self.cols[j][0]
                tenval = cost_for_letter[val]
                for i in range(j+1, -1, -1):
                    if self.hall[i] is not None:
                        break
                    ncost = self.cost + tenval*(self.dist(i, j)+1)
                    if ncost > upperbound:
                        continue
                    State(self.sethall(i, val), self.popcol(j), ncost).check()
                for i in range(j+2, 7):
                    if self.hall[i] is not None:
                        break
                    ncost = self.cost + tenval*(self.dist(i, j)+1)
                    if ncost > upperbound:
                        continue
                    State(self.sethall(i, val), self.popcol(j), ncost).check()

    # move-in dist (add 1 for move-out dist)
    def dist(self, hall, col):
        # 0 1   2   3   4   5 6
        #     0   1   2   3
        # 0 1 2 3 4 5 6 7 8 9 10
        depth = 4 - len(self.cols[col])
        col = col*2 + 2
        if hall == 6:
            hall = 10
        elif hall != 0:
            hall = hall*2 - 1
        return abs(hall - col) + depth

    def __repr__(self):
        return repr(self.hall) + repr(self.cols) + repr(self.cost)
    def __hash__(self):
        return self.hash
    def __eq__(self, oth):
        return self.hall == oth.hall and self.cols == oth.cols

fini_state = State((None,)*7, ((A,A,A,A),(B,B,B,B),(C,C,C,C),(D,D,D,D)), -1)
State((None,)*7, ((D,D,D,C),(C,C,B,D),(A,B,A,A),(B,A,C,B)), 0).check()
print(upperbound)
