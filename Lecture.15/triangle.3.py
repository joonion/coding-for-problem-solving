
def solve(T):
    n = len(T)
    for row in range(n - 2, -1, -1):
        for col in range(len(T[row])):
            T[row][col] += max(T[row+1][col], T[row+1][col+1])
    return T[0][0]

N = 100
T = []
for i in range(N):
    T.append(list(map(int, input().split())))
print(solve(T))



# for i in range(len(T)):
#     for j in range(len(T[i])):
#         print(T[i][j], end=" ")
#     print()
