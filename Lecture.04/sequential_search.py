import random

def sequential_search(nums, x):
    for i in range(len(nums)):
        if x == nums[i]:
            return i
    return -1

sequence = list(range(10, 100))   
N = 10
nums = random.sample(sequence, N) 
print(nums)
x = int(input("숫자를 입력하세요: "))
i = sequential_search(nums, x)
print(i, nums[i])
