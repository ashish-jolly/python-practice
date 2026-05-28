# program 1
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(3))

# program 2
def is_even_or_odd(number):
    if is_even(number):
        return "even"
    else:
        return "odd"
print(is_even_or_odd(2))

# program 3
def is_positive(number):
    if number > 0:
        return True
    else:
        return False
print(is_positive(0))

# program 4
def classify_number(number):
    if number == 0:
        return "zero"
    elif is_positive(number) and is_even(number):
        return "positive even"
    elif is_positive(number) and not is_even(number):
        return "positive odd"
    elif not is_positive(number) and is_even(number):
        return "negative even"
    elif not is_positive(number) and not is_even(number):
        return "negative odd"
print(classify_number(2))

# program 5
def grade_classifier(number):
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    elif number >= 60:
        return "D"
    else:
        return "F"
print(grade_classifier(79))