def collatz(n):
    # recursion 재귀 함수
    if n == 1:
        return [1]
    else:
        if n % 2 == 0:
            return [n] + collatz(n // 2)
        else:
            return [n] + collatz(3 * n + 1)

N, M = list(map(int, input().split()))
longest = 0
for i in range(N, M + 1):
    seq = collatz(i)
    if longest < len(seq):
        longest = len(seq)
print(longest)

