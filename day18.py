# DAY 18
# CONSOLIDATING WHAT I LEARNED IN MORE DEEPLY
# program 1
numbers = [4, 7, 2, 9, 1, 5]
for number in numbers:
    print(number)

# program 2
numbers = [4, 7, 2, 9, 1, 5, 8, 3]
for number in numbers:
    if number % 2 == 0:
        print(number)

# program 3
numbers = [3, 6, 1, 8, 2, 7]
total = 0
for number in numbers:
    total += number
print(total)

# program 4
numbers = [3, 6, 1, 8, 2, 7]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)

# program 5
numbers = [3, 6, 1, 8, 2, 7]
total = 0
for number in numbers:
    total += number
average = total / len(numbers)
count = 0
for number in numbers:
    if number > average:
        count += 1
print(count)