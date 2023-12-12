# this checks that a solution (stored in st as the array of offsets) is correct
def check():
    x = list(l)
    for i, j in enumerate(st):
        arity = r[i]
        for k in range(j, j+arity):
            if x[k] == '.':
                print('BAD')
            x[k] = '#'
    cs = []
    count = 0
    for ch in x:
        if ch == '#':
            count += 1
        else:
            if count:
                cs.append(count)
            count = 0
    if count:
        cs.append(count)
    if cs != r:
        print('BAD', cs, r, ''.join(x), l, st)
