# 400만 이하의 피보나치 수의 합

F = {0: 0, 1: 1}

def fib(n):
    if n not in F:
        F[n] = fib(n - 1) + fib(n - 2)
    return F[n]
    
fib(101)

sum = 0
for i in range(101):
    if F[i] % 2 == 0:
        sum += F[i]
    if F[i] >= 4000000:
        break
print(sum)