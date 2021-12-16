def fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
    
for n in range(101):
    print(n, ":", fib(n))