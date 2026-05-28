# DAY 11
# Functions
# program 1
def is_even(x):
    return x % 2 == 0
print(is_even(6))

def filter_evens(*args):
    result = []
    for number in (args):
        if is_even(number):
            result.append(number)
    return result
print(filter_evens(2, 5, 4, 7, 8))

# program 2
def multiply_all(*args):
    result = 1
    for number in (args):
        result = result * number
    return result
print(multiply_all(2, 3, 4, 2))

# list
# program 3
items = ["workout", "podcast", "shoulder rehab"]
items.remove("podcast")
print(items)

# program 4
items = ["badminton", "football", "cricket"]
items.pop(0)
print(items)

# program 5
items = ["laptop", "mobile phone", "charger"]
items.sort()
print(items)

# program 6
items = ["water", "food", "oxygen"]
items.reverse()
print(items)

# list slicing
# program 7
items = ["bread", "water", "meat", "cookies", "juice", "pen"]
print(items[0:3])

# program 8
items = ["bread", "water", "meat", "cookies", "juice", "pen"]
print(items[-2])

# program 9
items = ["bread", "water", "meat", "cookies", "juice", "pen"]
print(items[1:])

# program 10
items = ["bread", "water", "meat", "cookies", "juice", "pen"]
print(items[:2])

# Dictionaries
# program 11
dict1 = {"name": "Ashish", "age": 17, "city": "Kochi", "goal": "Top level backend engineer"}
print(dict1["name"])
dict1["day_coding"] = 11
dict1["age"] = 18
for key, value in dict1.items():
    print(key, value)
if "goal" in dict1:
    print("found")

