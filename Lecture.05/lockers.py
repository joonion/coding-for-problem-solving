n = 100
lockers = [-1] + [0 for i in range(1, 101)]

for N in range(1, 101):
    for j in range(N, 101, N):
        if (lockers[j] == 0):
            lockers[j] = j
        else:
            lockers[j] = 0

print(lockers)

open_lockers = []
for i in lockers:
    if i > 0:
        open_lockers.append(i)

print("열린 사물함의 개수:", len(open_lockers))
print("열린 사물함의 번호:", open_lockers)

import math
print(math.pi)