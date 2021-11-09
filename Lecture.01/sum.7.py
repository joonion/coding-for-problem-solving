def sum7(n):
    nums = list(range(1, n + 1))
    return sum(nums)

N = int(input("숫자를 입력하세요"))
S = sum7(N)
print(S)
