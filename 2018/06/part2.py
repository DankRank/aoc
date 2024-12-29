#!/usr/bin/env python3
import sys
m = [tuple(int(x) for x in line.rstrip().split(',')) for line in sys.stdin]

class Linear:
    __slots__ = 'a', 'b'
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'{self.__class__.__name__}({self.a!r}x + {self.b!r})'
    def __call__(self, x):
        return self.a*x + self.b
    def __add__(self, other):
        return Linear(self.a+other.a, self.b+other.b)
    def __sub__(self, other):
        return self + -other
    def __neg__(self):
        return Linear(-self.a, -self.b)
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def non_negative(self):
        if self.a == 0:
            if self.b < 0:
                return 0, 0
            else:
                return float('-inf'), float('inf')
        elif self.a > 0:
            # x >= -b/a (ceiling)
            x = (-self.b + (self.a-1))//self.a
            return x, float('inf')
        else:
            # x <= -b/a (floor)
            x = -self.b // self.a
            return float('-inf'), x+1
class Piecewise:
    __slots__ = 'funcs', 'splits'
    def __init__(self, funcs, splits):
        assert len(funcs) > 0
        assert len(funcs) == len(splits)+1
        i = 0
        while i < len(splits):
            if funcs[i] == funcs[i+1]:
                del funcs[i+1]
                del splits[i]
            else:
                i += 1
        self.funcs = funcs
        self.splits = splits
    def __repr__(self):
        return f'{self.__class__.__name__}(funcs={self.funcs!r}, splits={self.splits!r})'

    def get_pieces(self):
        for i in range(len(self.funcs)):
            start = self.splits[i-1] if i else float('-inf')
            stop = self.splits[i] if i < len(self.splits) else float('inf')
            yield self.funcs[i], start, stop
    def non_negative_ranges(self):
        for func, start, stop in self.get_pieces():
            startf, stopf = func.non_negative()
            start = max(start, startf)
            stop = min(stop, stopf)
            assert start != float('-inf')
            assert stop != float('inf')
            if start < stop:
                yield func, start, stop
    def non_negative_len(self):
        count = 0
        for func, start, stop in self.non_negative_ranges():
            count += max(0, stop-start)
        return count
    def non_negative_iter(self):
        for func, start, stop in self.non_negative_ranges():
            x = start
            y = func(x)
            while x < stop:
                assert y >= 0
                yield x, y
                x += 1
                y += func.a

    @staticmethod
    def const(b):
        return Piecewise([Linear(0, b)], [])
    @staticmethod
    def abssub(x0): # |x - x0|
        return Piecewise([Linear(-1, x0), Linear(1, -x0)], [x0])

    def __call__(self, x):
        for func, start, stop in self.get_pieces():
            if stop > x:
                return func(x)
        assert False
    def __add__(self, other):
        funcs = []
        splits = []
        g1 = self.get_pieces()
        g2 = other.get_pieces()
        func1, start1, stop1 = next(g1)
        func2, start2, stop2 = next(g2)
        while True:
            funcs.append(func1+func2)
            stop3 = min(stop1, stop2)
            # advance the piece that ends first
            if stop1 == stop2:
                if stop1 == float('inf'):
                    break
                func1, start1, stop1 = next(g1)
                func2, start2, stop2 = next(g2)
            elif stop1 == stop3:
                func1, start1, stop1 = next(g1)
            else:
                func2, start2, stop2 = next(g2)
            splits.append(stop3)
        return Piecewise(funcs, splits)
    def __sub__(self, other):
        return self + -other
    def __neg__(self):
        funcs = [-func for func in self.funcs]
        return Piecewise(funcs, self.splits.copy())

d = 32
d = 10000
xpiece = Piecewise.const(d-1)
ypiece = Piecewise.const(d-1)
for x, y in m:
    xpiece -= Piecewise.abssub(x)
    ypiece -= Piecewise.abssub(y)

count = 0
for x, y in ypiece.non_negative_iter():
    count += (xpiece - Piecewise.const(d-1 - y)).non_negative_len()
print(count)
