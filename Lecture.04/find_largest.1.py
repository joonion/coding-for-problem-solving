import random

def find_largest(nums):
    nums.sort()
    return nums[-1]

sequence = list(range(10, 100))   
N = 10
nums = random.sample(sequence, N) 
MAX = find_largest(nums)
print(nums)
print(MAX, max(nums))
