# DAY 30
# program 1
def filter_evens(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
print(filter_evens([4, 6, 7, 1, 3, 8, 12]))

# program 2
def filter_longer_than(words, number):
    filter_longer_than = []
    for word in words:
        if len(word) > number:
            filter_longer_than.append(word)
    return filter_longer_than
print(filter_longer_than(["cat", "elephant", "dog", "hippopotamus"], 4))

# program 3
def square_all(numbers):
    square_all = []
    for number in numbers:
        result = number ** 2
        square_all.append(result)
    return square_all
print(square_all([2, 3, 4]))

# program 4
def capitalize_all(words):
    capitalize_all = []
    for word in words:
        result = word.upper()
        capitalize_all.append(result)
    return capitalize_all
print(capitalize_all(["door", "carroms", "table"]))  

# program 5
def remove_duplicates(numbers):
    remove_duplicates = []
    for number in numbers:
        if number not in remove_duplicates:
            remove_duplicates.append(number)
    return remove_duplicates
print(remove_duplicates([1, 2, 2, 3, 1, 4]))