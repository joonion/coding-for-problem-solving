def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)

N = 10
S = sum2(N)
print(S)
