
def solve(row, col, T):
    if row == len(T):
        return 0
    else:
        return T[row][col] + max(solve(row+1, col, T), solve(row+1, col+1, T))

# # T = [ [3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
N = 100
T = []
for i in range(N):
    T.append(list(map(int, input().split())))
# print(T)   

print(solve(0, 0, T)),



# for i in range(len(T)):
#     for j in range(len(T[i])):
#         print(T[i][j], end=" ")
#     print()
    

print(2**99)