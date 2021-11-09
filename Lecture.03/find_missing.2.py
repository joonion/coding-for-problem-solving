import random

def find_missing2(S):
    n = len(S) + 1
    s = n * (n + 1) // 2    
    return s - sum(S)

nums = list(range(1, 11))
S = random.sample(nums, len(nums) - 1)
missing = find_missing2(S)
print(S)
print(missing)