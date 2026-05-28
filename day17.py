# DAY 17
# CONSOLIDATING WHAT I LEARNED MORE DEEPLY
# program 1
numbers = [1, 2, 3, 4, 5]
i = len(numbers) - 1
numbers2 = []
while i >= 0:
    numbers2.append(numbers[i])
    i -= 1
print(numbers2)

# program 2
numbers = [4, 7, 2, 9, 1, 5]
i = 0
largest = numbers[0]
second_largest = numbers[0]
while i < len(numbers):
    if numbers[i] > largest:
        second_largest = largest
        largest = numbers[i]
    elif numbers[i] > second_largest and numbers[i] < largest:
        second_largest = numbers[i]
    i += 1
print(second_largest)
    
