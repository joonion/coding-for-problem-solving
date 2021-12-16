
def hanoi(n, src, dst, via):
    if n == 1:
        print(src, "->", dst)
    else:
        hanoi(n - 1, src, via, dst)
        print(src, "->", dst)
        hanoi(n - 1, via, dst, src)

n = int(input("원판의 개수는? "))
hanoi(n, "A", "C", "B")
