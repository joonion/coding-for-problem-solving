import random

def find_missing(S):
    n = len(S) + 1
    return (n**2 + n) // 2 - sum(S) 

def find_missing_r(S, i):
    if i not in S:
        return i
    else:
        return find_missing_r(S, i-1)

N = int(input("자연수를 입력하세요: "))
nums = [i for i in range(1, N + 1)]
S = random.sample(nums, len(nums) - 1)
print(S)

missing = find_missing(S)
print(missing)

