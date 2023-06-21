#!/usr/bin/env python3
import os
import itertools
text = (input()+'\n').encode()
res = 0
for p in itertools.permutations(range(5, 10)):
    pipes = [os.pipe2(os.O_CLOEXEC) for i in range(5)]
    for i, a in enumerate(p):
        os.write(pipes[i-1][1],text)
        os.write(pipes[i-1][1],f'{a}\n'.encode())
    os.write(pipes[4][1],'0\n'.encode())
    for i in range(5):
        if os.fork() == 0:
            os.dup2(pipes[i-1][0], 0)
            os.dup2(pipes[i][1], 1)
            os.execl('./part2_unix_child.py', 'part2_unix_child.py')
            os._exit(1)
    for i in range(4):
        os.close(pipes[i][0])
        os.close(pipes[i][1])
    os.close(pipes[4][1])
    for i in range(5):
        os.waitpid(-1, 0)
    with open(pipes[4][0]) as f:
        res = max(res, int(f.readline().rstrip()))
print(res)
