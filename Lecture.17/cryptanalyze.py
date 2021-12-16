from collections import OrderedDict

def is_valid(letters, words):
    a, b, c = words
    n = len(c)
    carry = 0
    for i in range(n - 1, -1, -1):
        if any(letters[word[i]] is None for word in words):
            return True
        elif letters[a[i]] + letters[b[i]] + carry == letters[c[i]]:
            carry = 0
        elif letters[a[i]] + letters[b[i]] + carry == 10 + letters[c[i]]:
            carry = 1
        else:
            return False
        return True
    
def solve(letters, unassigned, nums, words):
    if len(unassigned) == 0:
        if (is_valid(letters, words)):
            return letters
        else:
            return None
    char = unassigned[0]
    for num in nums:
        letters[char] = num
        nums.remove(num)
        if is_valid(letters, words):
            solution = solve(letters, unassigned[1:], nums, words)
            if solution:
                return solution
        nums.add(num)
        letters[char] = None
    return False

def normalize(word, n):
    diff = n - len(word)
    return ['#'] * diff + word

def order_letters(words):
    n = len(words[2])
    letters = OrderedDict()
    for i in range(n - 1, -1, -1):
        for word in words:
            if word[i] not in letters:
                letters[word[i]] = None
    return letters

def cryptarithm(problem):
    words = list(map(list, problem))
    n = len(words[2])
    words[0] = normalize(words[0], n)
    words[1] = normalize(words[1], n)
    letters = order_letters(words)
    unassigned = [c for c in letters if c != '#']
    nums = set(range(0, 10))
    return solve(letters, unassigned, nums, words)

words = ["SEND", "MORE", "MONEY"]
solution = cryptarithm(words)
print(solution)

for word in words:
    for c in word:
        print(c, solution[c])
