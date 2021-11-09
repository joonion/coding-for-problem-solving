def sum3(n, m):
    if n == m:
        return n
    else:
        k = (n + m) // 2
        return sum3(n, k) + sum3(k + 1, m)

N = 10
S = sum3(1, N)
print(S)
