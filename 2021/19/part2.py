#!/usr/bin/env python3
scanners = []
try:
    while True:
        input()
        scanner = set()
        scanners.append(scanner)
        while True:
            s = input()
            if s == '':
                break
            scanner.add(tuple(map(int, s.split(','))))
except EOFError:
    pass
transforms = [
    lambda p: ( p[0],  p[1],  p[2]),
    lambda p: ( p[0],  p[2], -p[1]),
    lambda p: ( p[0], -p[1], -p[2]),
    lambda p: ( p[0], -p[2],  p[1]),
    lambda p: (-p[0],  p[1], -p[2]),
    lambda p: (-p[0],  p[2],  p[1]),
    lambda p: (-p[0], -p[1],  p[2]),
    lambda p: (-p[0], -p[2], -p[1]),
    lambda p: ( p[1], -p[0],  p[2]),
    lambda p: ( p[1], -p[2], -p[0]),
    lambda p: ( p[1],  p[0], -p[2]),
    lambda p: ( p[1],  p[2],  p[0]),
    lambda p: (-p[1], -p[0], -p[2]),
    lambda p: (-p[1], -p[2],  p[0]),
    lambda p: (-p[1],  p[0],  p[2]),
    lambda p: (-p[1],  p[2], -p[0]),
    lambda p: ( p[2],  p[1], -p[0]),
    lambda p: ( p[2],  p[0],  p[1]),
    lambda p: ( p[2], -p[1],  p[0]),
    lambda p: ( p[2], -p[0], -p[1]),
    lambda p: (-p[2],  p[1],  p[0]),
    lambda p: (-p[2],  p[0], -p[1]),
    lambda p: (-p[2], -p[1], -p[0]),
    lambda p: (-p[2], -p[0],  p[1]),
]
known_beacons = {x for x in scanners[0]}
undecided = list(scanners[1:])
scanners = [(0,0,0)]
while len(undecided) > 0:
    for pt1 in list(known_beacons):
        for beacons in list(undecided):
            for xf in transforms:
                rotated = list(map(xf, beacons))
                for pt2 in rotated:
                    d = pt1[0]-pt2[0], pt1[1]-pt2[1], pt1[2]-pt2[2]
                    translated = set(map(lambda p: (p[0]+d[0], p[1]+d[1], p[2]+d[2]), rotated))
                    if len(translated & known_beacons) >= 12:
                        known_beacons.update(translated)
                        undecided.remove(beacons)
                        scanners.append(d)
                        break
                else:
                    continue
                break
def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])
print(max(*(dist(scanners[i], scanners[j]) for i in range(len(scanners)) for j in range(i+1, len(scanners)))))
