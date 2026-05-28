# DAY 25 OF PROGRAMMING
# program 1
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(3))

# program 2
def get_max(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2
print(get_max(8, 8))

# program 3
def count_vowels(word):
    count_vowels = 0
    vowels = ("a", "e", "i", "o", "u")
    for letter in word:
        if letter in vowels:
            count_vowels += 1
    return count_vowels
print(count_vowels("programming"))