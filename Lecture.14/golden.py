F = {0: 0, 1: 1}

def fib(n):
    if n not in F:
        F[n] = fib(n - 1) + fib(n - 2)
    return F[n]
    
fib(101)
print(F)
t
for i in range(1, 101):
    print(F[i+1], "/", F[i], ":", F[i + 1] / F[i])


    