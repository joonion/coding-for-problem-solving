def to_arabic(roman):
    table  = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    n = len(roman)
    number = 0
    for i in range(n):
        if i < n - 1 and table[roman[i]] < table[roman[i + 1]]:
            number -= table[roman[i]]
        else:
            number += table[roman[i]]
    return number

def to_roman(N):
    table={1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C',  90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    roman = ""
    for key in table.keys():
        while N >= key:
            roman += table[key]
            N -= key
    return roman

romans = ["CCCLXIX", "LXXX", "XXIX", "CLV", "XIV", "CDXCII", "CCCXLVIII", "CCCI", "CDLXIX", "CDXCIX"]
nums = [369, 80, 29, 155, 14, 492, 348, 301, 469, 499]

n = to_arabic(input())
m = to_arabic(input())
print(to_roman(n + m))



