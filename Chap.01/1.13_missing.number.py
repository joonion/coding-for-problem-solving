def missing_number(N, numbers):
    check = [False] * (N + 1)
    for n in numbers:
        check[n] = True
    for x in range(1, N + 1):
        if check[x] is False:
            return x
    return None

N = int(input())
numbers = list(map(int, input().split()))
print(missing_number(N, numbers))
