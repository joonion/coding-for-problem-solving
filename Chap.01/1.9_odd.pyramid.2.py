def sum_of_pyramid2(N):
    if N == 1:
        return 1, 1
    else:
        S, k = sum_of_pyramid2(N - 1)
        for _ in range(N):
            k += 2
            S += k
        return S, k

N = int(input())
S, k = sum_of_pyramid2(N)
print(S)
