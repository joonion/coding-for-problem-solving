def sum_of_pyramid(N):
    S, k = 0, 1
    for i in range(1, N + 1):
        for _ in range(i):
            S += k
            k += 2
    return S

N = int(input())
print(sum_of_pyramid(N))
