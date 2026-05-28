# DAY 19
# CONSOLIDATING WHAT I LEARNED MORE DEEPLY
# program 1
words = ["cat", "elephant", "dog", "python", "ox", "tiger"]
words2 = []
for word in words:
    if len(word) > 4:
        words2.append(word)
print(words2)

# program 2
numbers = [3, 6, 1, 8, 2, 7, 4, 5]
total = 0
for number in numbers:
    if number % 2 == 0:
        total += number
print(total)

# program 3
numbers = [4, 7, 2, 9, 1, 5, 8, 3]
for number in numbers:
    if number % 2 == 0:
        print(number, "even")
    else:
        print(number, "odd")

# program 4
numbers = [3, 6, 1, 8, 2, 7]
numbers2 = []
for number in numbers:
    numbers2.append(number * 2)
print(numbers2)

# program 5
words = ["cat", "elephant", "dog", "python", "ox"]
length_of_words = []
for word in words:
    length_of_words.append(len(word))
print(length_of_words)

# program 6
numbers = [5, 10, 15, 20, 25]
total = 0
for number in numbers:
    total += number
average = total / len(numbers)
print(average)

# program 7
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = []
for number in list1:
    if number in list2:
        list3.append(number)
print(list3)
