import random

def find_largest(nums):
    largest = nums[0]
    for i in range(1, len(nums)):
        if largest < nums[i]:
            largest = nums[i]
    return largest

sequence = list(range(10, 100))   
N = 10
nums = random.sample(sequence, N) 
MAX = find_largest(nums)
print(nums)
print(MAX, max(nums))