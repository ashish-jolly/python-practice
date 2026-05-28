# DAY 29
# program 1
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(3))

# program 2
def reverse_string(word):
    reverse = word[::-1]
    return reverse
print(reverse_string("programming"))

# program 3
def sum_list(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total += number
    return total
print(sum_list([3, 4, 7]))

# program 4
def most_frequent_character(sentence):
    result = {}
    for letter in sentence:
        if letter == " ":
            continue
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    most_frequent_character = ""
    highest_count = 0
    for key in result:
        if result[key] > highest_count:
            highest_count = result[key]
            most_frequent_character = key
    return most_frequent_character
print(most_frequent_character("hello world"))

        
