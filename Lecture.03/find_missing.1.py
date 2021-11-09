import random

def find_missing1(S):
    n = len(S) + 1
    flags = [True] + [False] * n
    for i in range(len(S)):
        flags[S[i]] = True
    for i in range(1, n + 1):
        if flags[i] == False:
            return i
    return -1

nums = list(range(1, 11))
S = random.sample(nums, len(nums) - 1)
missing = find_missing1(S)
print(S)
print(missing)
