def sum5(n):
    nums = []
    for i in range(1, n + 1):
        nums.append(i)
    return sum(nums)

N = 10
S = sum5(N)
print(S)