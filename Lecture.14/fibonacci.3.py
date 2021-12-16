F = {0: 0, 1: 1}

def fib(n):
    if n not in F:
        F[n] = fib(n - 1) + fib(n - 2)
    return F[n]
    
for n in range(101):
    print(n, ":", fib(n))