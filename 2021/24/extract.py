#!/usr/bin/env python3
def extract_constants(f):
    a = []
    b = []
    c = []
    for i in range(14):
        f.readline() # inp w
        f.readline() # mul x 0
        f.readline() # add x z
        f.readline() # mod x 26
        c.append(int(f.readline().split()[2])) # div z C
        a.append(int(f.readline().split()[2])) # add x A
        f.readline() # eql x w
        f.readline() # eql x 0
        f.readline() # mul y 0
        f.readline() # add y 25
        f.readline() # mul y x
        f.readline() # add y 1
        f.readline() # mul z y
        f.readline() # mul y 0
        f.readline() # add y w
        b.append(int(f.readline().split()[2])) # add y B
        f.readline() # mul y x
        f.readline() # add z y
    return a, b, c
def generate_expander(a, b, c):
    s = 'lambda i: (\n'
    stack = []
    index = 0
    for i in range(14):
        if c[i] == 26:
            j, jndex  = stack.pop()
            s += f'    i[{jndex}] + {b[j]} - {-a[i]},\n'
        else:
            s += f'    i[{index}],\n'
            stack.append((i, index))
            index += 1
    s += ')'
    return s
if __name__ == '__main__':
    import sys
    a, b, c = extract_constants(sys.stdin)
    print('a = ' + str(a))
    print('b = ' + str(b))
    print('c = ' + str(c))
    print('expand = ' + generate_expander(a, b, c))
