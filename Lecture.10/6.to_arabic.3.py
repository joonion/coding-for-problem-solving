table  = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
romans = ["CCCLXIX", "LXXX", "XXIX", "CLV", "XIV", "CDXCII", "CCCXLVIII", "CCCI", "CDLXIX", "CDXCIX"]

def to_arabic(roman):
    n = len(roman)
    number = 0
    for i in range(n):
        if i < n - 1 and table[roman[i]] < table[roman[i + 1]]:
            number -= table[roman[i]]
        else:
            number += table[roman[i]]
    return number

for roman in romans:
    print(roman, ":", to_arabic(roman))
    