# n = 10000000
# sieve = [False, False] + [True] * (n - 1)

# count = 0
# for i in range(2, n + 1):
#     if sieve[i] == True:
#         count += 1
#         for j in range(i * 2, n + 1, i):
#             sieve[j] = False
# print(count)

print((2**7-1)**2)
print((2**31-1)**2)