from itertools import permutations
from time import time

def toint(s, map):
    value = 0
    for i in range(len(s)):
        value *= 10
        value += map[s[i]]
    return value

def is_valid(n, m, s, map):
    if 0 in [map[n[0]], map[m[0]], map[s[0]]]:
        return False        
    else:
        a = toint(n, map)
        b = toint(m, map)
        c = toint(s, map)
        return a + b == c

def solve(n, m, s):
    solutions = []
    letters = set(n + m + s)
    digits = [i for i in range(10)]
    perms = list(permutations(digits, len(letters)))
    for perm in perms:
        map = {k:v for (k, v) in zip(letters, perm)}
        if is_valid(n, m, s, map):
            solutions.append(map)
    return solutions

n, m, s = input().split()
start = time()
solutions = solve(n, m, s)
duration = time() - start
for map in solutions:
    print(n, toint(n, map))
    print(m, toint(m, map))
    print(s, toint(s, map))
print("Elapsed:", duration)