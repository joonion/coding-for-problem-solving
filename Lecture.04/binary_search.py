import random

def binary_search(nums, x):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == nums[mid]:
            return mid
        elif x < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

sequence = list(range(10, 100))   
N = 10
nums = random.sample(sequence, N) 
nums.sort()
print(nums)
x = int(input("숫자를 입력하세요: "))
M, m = binary_search(nums, x)
print(M, m)
