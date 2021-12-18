#!/usr/bin/env python3
class Pair:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.val = None
        self.parent = None
        lhs.parent = self
        rhs.parent = self
    def __repr__(self):
        return '[%s,%s]' % (self.lhs, self.rhs)
class Number:
    def __init__(self, val):
        self.lhs = None
        self.rhs = None
        self.val = val
        self.parent = None
    def __repr__(self):
        return repr(self.val)
def pred(node):
    while node.parent is not None:
        if node.parent.rhs is node:
            node = node.parent.lhs
            while node.rhs is not None:
                node = node.rhs
            return node
        node = node.parent
    return None
def succ(node):
    while node.parent is not None:
        if node.parent.lhs is node:
            node = node.parent.rhs
            while node.lhs is not None:
                node = node.lhs
            return node
        node = node.parent
    return None
def replacenode(node, newnode):
    newnode.parent = node.parent
    # won't work for root node
    if node.parent.lhs is node:
        node.parent.lhs = newnode
    else:
        node.parent.rhs = newnode
class ReduceAgainException(Exception):
    pass
def explode(node, level=0):
    if isinstance(node, Pair):
        if level == 4:
            p = pred(node)
            s = succ(node)
            if p is not None:
                p.val += node.lhs.val
            if s is not None:
                s.val += node.rhs.val
            replacenode(node, Number(0))
            raise ReduceAgainException()
        else:
            explode(node.lhs, level+1)
            explode(node.rhs, level+1)
def split(node):
    if isinstance(node, Number):
        if node.val > 9:
            replacenode(node, Pair(Number(node.val//2), Number((node.val+1)//2)))
            raise ReduceAgainException()
    else:
        split(node.lhs)
        split(node.rhs)
def reduction(tree):
    while True:
        try:
            explode(tree)
            split(tree)
            break
        except ReduceAgainException:
            pass
def parsePair(s):
    if s[0].isdigit():
        return Number(int(s[0])), s[1:]
    else:
        lhs, s = parsePair(s[1:])
        rhs, s = parsePair(s[1:])
        return Pair(lhs, rhs), s[1:]

tree = None
try:
    while True:
        ntree, _ = parsePair(input())
        if tree is None:
            tree = ntree
        else:
            tree = Pair(tree, ntree)
            reduction(tree)
except EOFError:
    pass

def magnitude(node):
    if isinstance(node, Pair):
        return 3*magnitude(node.lhs) + 2*magnitude(node.rhs)
    else:
        return node.val
print(magnitude(tree))
