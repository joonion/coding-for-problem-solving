table={1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C',  90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

def to_roman(N):
    roman = ""
    for key in table.keys():
        while N >= key:
            roman += table[key]
            N -= key
    return roman

nums = [369, 80, 29, 155, 14, 492, 348, 301, 469, 499]
for num in nums:
    print(num, ":", to_roman(num))

num = 398
print(num, ":", to_roman(num))
