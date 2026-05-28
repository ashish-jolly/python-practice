# DAY 13
# consolidation
# program 1
def summarize(*args):
    return {"count": len(args), "total": sum(args), "average": sum(args) / len(args), "max": max(args), "min": min(args)}
print(summarize(5, 10, 20, 9, 6))

# program 2
def categorize(numbers):
    positive = []
    negative = []
    zero = []
    for number in numbers:
        if number > 0:
            positive.append(number)
        elif number < 0:
            negative.append(number)
        else:
            zero.append(number)
    return {"positive": positive, "negative": negative, "zero": zero}
print(categorize([3, -1, 0, 5, -2, 0, 7, -4]))

# program 3
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key in dict2:
        if key in result:
            result[key] += dict2[key]
        else:
            result[key] = dict2[key]
    return result
print(merge_dicts(dict1 = {"a": 1, "b": 2, "c": 3}, dict2 = {"b": 4, "c": 5, "d": 6}))

# program 4
def find_duplicates(numbers):
    result = set()
    seen = set()
    for number in (numbers):
        if number in seen:
            result.add(number)
        else:
            seen.add(number)
    return result
print(find_duplicates([1, 2, 3, 2, 4, 3, 5, 1]))

# program 5
def  word_lengths(sentence):
    result = {}
    words = sentence.split()
    for word in words:
        result[word] = len(word)
    return result
print(word_lengths("I love backend engineering"))

# Chat GPT Test
# problem 1
nums = [3, 8, 2, 10, 5]
i = 0
while i in len(nums):
    if i > 5 (nums):
        i += 1
print(nums)
        