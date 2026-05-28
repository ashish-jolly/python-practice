# DAY 16
# CONSOLIDATION OF WHAT I LEARNED IN MORE DEEPLY
# program 1

numbers = [4, 7, 2, 9, 1, 5]
i = 0
smallest = numbers[0]
while i < len(numbers):
    if numbers[i] < smallest:
        smallest = numbers[i]
    i += 1
print(smallest)

# program 2
numbers = [2, 8, 1, 6, 3, 9, 4, 7]
i = 0
count = 0
while i < len(numbers):
    if numbers[i] > 5:
        count += 1
    i += 1
print(count)

# program 3
numbers = [4, 7, 2, 9, 1, 5, 8, 3]
i = 0
count1 = 0
count2 = 0
while i > len(numbers):
    if numbers[i] % 2 == 0:
        count1 += 1
    elif numbers[i] % 2 == 1:
        count2 += 1
    i += 1
print(count1)
print(count2)