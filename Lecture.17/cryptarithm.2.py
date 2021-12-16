from itertools import permutations
from time import time

def toint(s, map):
    value = 0
    for i in range(len(s)):
        value += map[s[i]] * (10**i)
    return value

def promising(i, x, y, z, map):
    a = toint(x[:(i+1)], map)
    b = toint(y[:(i+1)], map)
    c = toint(z[:(i+1)], map)
    limit = 10 ** (max(len(str(a)), len(str(b))))
    return (a + b) % limit == c % limit

def is_valid(x, y, z, map):
    if 0 in [map[x[-1]], map[y[-1]], map[z[-1]]]:
        return False        
    a = str(toint(x, map))
    b = str(toint(y, map))
    c = str(toint(z, map))
    return int(a) + int(b) == int(c)
            
def solveto(i, x, y, z, map):
    global solved
    print(i, map, solved)
    if i == max(len(x), len(y)):
        if is_valid(x, y, z, map):
            solved.append(map)
            print(solved)
    else:
        letters = set(x[i] + y[i] + z[i]) - map.keys()
        digits = set(i for i in range(10)) - set(map.values())
        perms = list(permutations(digits, len(letters)))
        for perm in perms:
            for (k, v) in zip(letters, perm):
                map[k] = v
            if promising(i, x, y, z, map):
                solveto(i + 1, x, y, z, map)
            for k in letters:
                map.pop(k)

def solve(n, m, s):
    empty = {}
    return solveto(0, n[::-1], m[::-1], s[::-1], empty)

solved = []

if __name__=='__main__':
    n, m, s = "SEND", "MORE", "MONEY"
    start = time()
    solve(n, m, s)
    print(solved)
    duration = time() - start
    print("Elapsed:", duration)
    for map in solved:
        print(n, toint(n, map))
        print(m, toint(m, map))
        print(s, toint(s, map))
