def summation4(N, M):
    if N == M:
        return N
    else:
        mid = (N + M) // 2
        return summation4(N, mid) + summation4(mid + 1, M)

N = int(input())
print(summation4(1, N))
