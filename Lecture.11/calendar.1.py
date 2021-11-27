year, month = 2021, 12
day_of_week = 3 # 수요일

print(year, "년", month, "월:")
for day in ['일', '월', '화', '수', '목', '금', '토']:
    print(' ', day, end = ' ')
print()

for _ in range(day_of_week):
    print('    ', end=' ')
     
# 날짜 계산
def leapyear(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

num_of_days = 30 if month in [4, 6, 9, 11] else 31
if month == 2:
    num_of_days = 29 if leapyear(year) else 28
    
for day in range(1, num_of_days + 1):
    if day < 10:
        print('  ', day, end = ' ')
    else:
        print(' ', day, end = ' ')
    if (day_of_week + day) % 7 == 0:
        print()
print()