F = {0: 0, 1: 1}

def fib(n):
    if n not in F:
        F[n] = fib(n - 1) + fib(n - 2)
    return F[n]
    
fib(101)
print(F)
    