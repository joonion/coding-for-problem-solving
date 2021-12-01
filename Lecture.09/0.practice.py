N = int(input())
for i in range(N):
    S = input().split()
    print(S)
    # ......
    for string in S:
        if string.upper() == "THE":
            count += 1
        