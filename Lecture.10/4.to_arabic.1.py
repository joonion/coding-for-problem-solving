table  = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

roman = "MDCLXVI"
number = 0
for ch in roman:
    number += table[ch]
print(number)