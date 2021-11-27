def collatz(n):
    # recursion 재귀 함수
    if n == 1:
        print(1)
        return 
    else:
        print(n)
        if n % 2 == 0:
            collatz(n // 2)
        else:
            collatz(3 * n + 1)
        
n = int(input("양의 정수를 입력하세요: "))
collatz(n)
