# DAY 15
# CONSOLIDATION OF WHAT I LEARNED
# program 1
numbers = [2, 8, 1, 6, 3, 9, 4, 7]
i = 0
while i < len(numbers):
    if numbers[i] > 5:
        print(numbers[i])
    i += 1

# program 2
numbers = [4, 7, 2, 9, 1, 5]
x = 0
total = 0
while x < len(numbers):
    total += numbers[x]
    x += 1
print(total)

# program 3
numbers = [4, 7, 2, 9, 1, 5]
i = 0
largest = numbers[0]
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i += 1
print(largest)
