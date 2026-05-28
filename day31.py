# DAY 31
# program 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
set1 = set()
for number in numbers:
    set1.add(number)
print(set1)

# program 2
tuple1 = (10, 20, 30, 40, 50)
length = len(tuple1)
print(tuple1[0])
print(tuple1[4])
print(length)

# program 3
numbers = [1, 2, 3, 4, 5]
result = [number * 2 for number in numbers]
print(result)

# program 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# program 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(square_even_numbers)

# program 5
items = ["apple", "banana", "cat", "dog", "elephant"]
longer_than_4 = [word for word in items if len(word) > 4]
print(longer_than_4)

# program 6
items = ["apple", "banana", "cat", "dog", "elephant"]
result = [len(word) for word in words if word[0] "a", "e", "i", "o", "u"]
print(result)
