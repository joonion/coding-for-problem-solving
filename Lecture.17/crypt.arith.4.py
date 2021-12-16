from itertools import permutations
from time import time

def to_int(reversed, map):
    value = 0
    for i in range(len(reversed)):
        value += map[reversed[i]] * (10 ** i)
    return value

def is_valid(w1, w2, w3, map):
    leadings = [map[w1[0]], map[w2[0]], map[w3[0]]]
    if 0 in leadings:
        return False
    a = to_int(w1[::-1], map)
    b = to_int(w2[::-1], map)
    c = to_int(w3[::-1], map)
    return a + b == c

def promising(i, r1, r2, r3, map):
    n = (10 ** (i + 1))
    a = to_int(r1, map)
    b = to_int(r2, map)
    c = to_int(r3, map)
    return (a + b) % n == c % n

def solveto(n, i, map, solved, r1, r2, r3):
    if i == n:
        if is_valid(r1[::-1], r2[::-1], r3[::-1], map):
            solved.append(map.copy())
    else:
        s1, s2, s3 = r1[:(i+1)], r2[:(i+1)], r3[:(i+1)]
        letters = set(s1[i] + s2[i] + s3[i]) - set(map.keys())
        digits = set(range(10)) - set(map.values())
        for perm in permutations(digits, len(letters)):
            for k, v in zip(letters, perm):
                map[k] = v
            if promising(i, s1, s2, s3, map):
                solveto(n, i + 1, map, solved, r1, r2, r3)
            for k in letters:
                map.pop(k)

def solve(w1, w2, w3):
    n = max(len(w1), len(w2))
    map = {}
    solved = []
    r1, r2, r3 = w1[::-1], w2[::-1], w3[::-1]
    solveto(n, 0, map, solved, r1, r2, r3)
    return solved

# Cryptarithmetic by the Backtracking
w1, w2, w3 = input().split()
start = time()
solved = solve(w1, w2, w3)
print("실행시간:", time() - start)
print(len(solved))
for map in solved:
    print(w1, to_int(w1[::-1], map))
    print(w2, to_int(w2[::-1], map))
    print(w3, to_int(w3[::-1], map))
   