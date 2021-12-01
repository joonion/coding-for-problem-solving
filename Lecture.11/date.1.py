year, month, day = 2021, 11, 25
n = 1000

def leapyear(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

def invalid(year, month, day):
    num_of_days = 30 if month in [4, 6, 9, 11] else 31
    if month == 2:
        num_of_days = 29 if leapyear(year) else 28
    return day > num_of_days

for _ in range(n):
    day += 1
    if invalid(year, month, day):
        day, month = 1, month + 1
        if month > 12:
            month, year = 1, year + 1

print(year, month, day)
