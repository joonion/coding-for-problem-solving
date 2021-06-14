def summation3(N, S):
    if N == 0:
        return S
    else:
        return summation3(N - 1, N + S)

N = int(input())
print(summation3(N, 0))
