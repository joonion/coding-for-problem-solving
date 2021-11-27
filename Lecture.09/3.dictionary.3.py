table = {"깍두기":1, "민혀기":2, "서주니":3}
print(table.keys())
print(table.values())
for item in table.items():
    key = item[0]
    value = item[1]
    print(key, ":", value)
table["깍두기"] = 4
print(table)