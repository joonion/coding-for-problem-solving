def to_arabic(char):
    if char == "I":
        return 1
    elif char == "V":
        return 5
    elif char == "X":
        return 10
    elif char == "L":
        return 50
    elif char == "C":
        return 100
    elif char == "D":
        return 500
    elif char == "M":
        return 1000

romans = "IVXLCDM"
for char in romans:
    print(char, ":", to_arabic(char))
  