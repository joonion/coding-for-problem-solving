def sum1(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

N = 10000000
S = sum1(N)
print(S)
