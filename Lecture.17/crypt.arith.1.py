from itertools import permutations

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

def solve(w1, w2, w3):
    letters = sorted(set(w1 + w2 + w3))
    digits = list(range(10))
    solved = []
    for perm in permutations(digits, len(letters)):
        map = {k:v for k, v in zip(letters, perm)}
        if is_valid(w1, w2, w3, map):
            solved.append(map)
    return solved

# Cryptarithmetic by the Brute-Force
w1, w2, w3 = "SEND", "MORE", "MONEY"
solved = solve(w1, w2, w3)
for map in solved:
    print(w1, to_int(w1[::-1], map))
    print(w2, to_int(w2[::-1], map))
    print(w3, to_int(w3[::-1], map))
    