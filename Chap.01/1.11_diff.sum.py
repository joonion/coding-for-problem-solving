def diff_of_sums(N):
    return N * (N - 1) * (N + 1) * (N + 2) // 4

N = int(input())
print(diff_of_sums(N))
