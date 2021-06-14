def summation4(M, N):
    if M == N:
        return M
    else:
        mid = (M + N) // 2
        return summation4(M, mid) + summation4(mid + 1, N)

N = int(input())
print(summation4(1, N))
