table = {}
N = int(input())
count1, count2 = 0, 0
for i in range(N):
    words = input().split()
    for word in words:
        if word.upper() == "THE":
            count1 += 1
        elif word.upper() == "A" or word.upper() == "AN":
            count2 += 1
print(count1)
print(count2)