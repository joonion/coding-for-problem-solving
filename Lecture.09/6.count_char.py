table = {}
N = int(input())
for i in range(N):
    string = input()
    for ch in string:
        if ch.isalpha():
            upper = ch.upper()
            if upper in table:
                table[upper] += 1
            else:
                table[upper] = 1
print(max(table.values()))