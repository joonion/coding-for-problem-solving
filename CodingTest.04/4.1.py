def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

N = int(input())
nums = list(map(int, input().split()))

sums = [0] * len(nums)
for i in range(len(nums)):
    sums[i] = sum_digits(nums[i])

# largest: 각 자릿수의 합이 가장 큰 위치(인덱스)    
largest = 0
for i in range(len(nums)):
    if (sums[largest] < sums[i]):
        largest = i
        
print(nums[largest])
