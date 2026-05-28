# DAY 26
# program 1
def reversed_string(word):
    letter = word[::-1]
    return letter
print(reversed_string("backend engineer"))

# program 2
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(sum_list([10, 20, 30]))

# program 3
def is_palindrome(word):
    palindrome = word == word[::-1]
    return palindrome
print(is_palindrome("racecar"))