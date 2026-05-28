# DAY 32
# program 1
words = ["apple", "banana", "cat", "dog", "elephant"]
result = [len(word) for word in words if word[0] in ("a", "e", "i", "o", "u")]
print(result)

# program 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [0 if number % 2 == 1 else number for number in numbers]
print(result)

# program 3
words = ["hello", "world", "python", "is", "great"]
result = [word.upper() for word in words if len(word) > 3]
print(result)

# proram 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["even" if number % 2 == 0 else "odd" for number in numbers]
print(result)

# program 5
try:
    number = int(input("enter a number"))
    result = 100 / number
    print(result)
except:
    print("cannot divide by zero")