def summation(N):
    S = 0
    for i in range(1, N + 1):
        S += i
    return S

N = int(input())

from time import time

start = time()
S = summation(N)
end = time()
print('실행에 걸린 시간:', end - start)



