def collatz(n):
    # recursion 재귀 함수
    if n == 1:
        return [1]
    else:
        if n % 2 == 0:
            return [n] + collatz(n // 2)
        else:
            return [n] + collatz(3 * n + 1)
        
n = int(input("양의 정수를 입력하세요: "))
seq = collatz(n)
print(seq)
for i in range(len(seq)):
    print(seq[i], end=" ")
print(len(seq))



