def collatz(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)
    
n = int(input("양의 정수를 입력하세요: "))
collatz(n)
