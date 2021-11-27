def collatz(n):
    seq = []
    while n > 1:
        seq.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    seq.append(n)
    return seq

N, M = list(map(int, input().split()))
longest = 0
for i in range(N, M + 1):
    seq = collatz(i)
    if longest < len(seq):
        longest = len(seq)
print(longest)