def josephus(n, k):
    q = [i for i in range(1, n + 1)]
    j = 0
    while len(q) > 1:
        j = (j + k - 1) % len(q)
        q.pop(j)
    return q[0]
    
print(josephus(41, 3))