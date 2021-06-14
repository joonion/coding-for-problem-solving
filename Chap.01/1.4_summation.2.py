def summation2(N):
    if N == 1:
        return 1
    else:
        return N + summation2(N - 1)

N = int(input())
print(summation2(N))
