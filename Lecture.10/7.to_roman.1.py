table={1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C',  90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

def to_roman(N):
    roman = ""
    for key in table.keys():
        while N >= key:
            roman += table[key]
            N -= key
    return roman

print(to_roman(1666))
print(to_roman(1444))
print(to_roman(1999))
