
def solve(row, col, T, C):
    if row == len(T):
        return 0        
    elif C[row][col] == 0:
        C[row][col] = T[row][col] + max(solve(row+1, col, T, C), solve(row+1, col+1, T, C))
    return C[row][col]

N = 100
T = []
C = []
for i in range(N):
    T.append(list(map(int, input().split())))
    C.append([0] * len(T[i]))
print(solve(0, 0, T, C))



# for i in range(len(T)):
#     for j in range(len(T[i])):
#         print(T[i][j], end=" ")
#     print()
