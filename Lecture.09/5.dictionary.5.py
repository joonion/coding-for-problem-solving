string = "How are you? I'm fine, and you?"
table = {}
for ch in string:
    if ch.isalpha():
        upper = ch.upper()
        if upper not in table:
            table[upper] = 1
        else:
            table[upper] += 1
for key in table:
    print(key, ":", table[key])