# DAY 21
# CONSOLIDATING DEEPLY WHAT I LEARNED
# program 1
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
dict1 = {}
for word in words:
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1
print(dict1)

# program 2
numbers = [1, 2, 3, 2, 1, 3, 3, 4, 1]
dict1 = {}
for number in numbers:
    if number in dict1:
        dict1[number] += 1
    else:
        dict1[number] = 1
print(dict1)

# program 3
sentence = "hello world"
dict1 = {}
for letter in sentence:
    if letter == " ":
        continue
    if letter in dict1:
        dict1[letter] += 1
    else:
        dict1[letter] = 1
print(dict1)
    