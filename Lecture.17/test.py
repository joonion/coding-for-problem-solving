def fun(solutions, map):
    map[1] = '홍길동'
    solutions.append(map)

solutions = []
fun(solutions, {})
print(solutions)