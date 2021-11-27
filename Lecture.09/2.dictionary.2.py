table = {1:"깍두기", 2:"민혀기", 3:"서주니"}
table[4] = "태혀니"
for key in table.keys():
    print(key, ":", table[key])
table.pop(2)
for key in table.keys():
    print(key, ":", table[key])
