def missing_number2(N, numbers):
    S = N * (N + 1) // 2
    for n in numbers:
        S -= n
    return S

N = int(input())
numbers = list(map(int, input().split()))
print(missing_number2(N, numbers))
