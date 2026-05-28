# DAY 27
# program 1
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(25))

# program 2
def find_longest_word(list_of_words):
    longest_word = ""
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
print(find_longest_word(["towel", "door", "laptop"]))

# program 3
def count_words(words_in_sentence):
    word = words_in_sentence.split()
    return len(word)
print(count_words("I am a programmer"))

# program 4
def is_positive(number):
    if number > 0:
        return True
    else:
        return False
print(is_positive(0))

# program 5
def multiply(number1, number2, number3):
    result = number1 * number2 * number3
    return result
print(multiply(3, 10, 5))
