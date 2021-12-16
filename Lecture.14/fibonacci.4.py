
def fib(n):
    F = [0, 1]
    if n <= 1:
        return F[n]
    else:
        for i in range(2, n + 1):
            F.append(F[i - 1] + F[i - 2])
        return F[n]
    
for n in range(101):
    print(n, ":", fib(n))