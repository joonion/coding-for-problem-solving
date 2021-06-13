def summation(N):
    S = 0
    for i in range(1, N + 1):
        S += i
    return S

N = int(input())
print(summation(N))
