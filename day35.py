# DAY 35
# program 1
try:
    a = int(input("first number"))
    b = int(input("second number"))
    op = (input("+, -, *, /"))
    result = None
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        print("invalid operator")
    print("result:", result)
except ValueError:
    print("invalid input, try again")
except ZeroDivisionError:
    print("cannot divid by zero")

# program 2
try:
    age = int(input("enter your age"))
    if age < 18:
        print("you are a minor")
    else:
        print("you are an adult")
except ValueError:
    print("invalid input, try again")

# program 3
try:
    celcius = int(input("enter current celcius"))
    in_fahrenheit = (celcius * 9/5) + 32
    print(in_fahrenheit)
except ValueError:
    print("invalid input, try again")

# program 4
username = input("enter a username")
password = input("enter a password")
if username == "admin" and password == "1234":
    print("login succesful")
else:
    print("invalid credentials")

# program 5
secret_number = 7
try:
    guess = int(input("guess a number"))
    if guess > secret_number:
        print("high")
    elif guess < secret_number:
        print("low")
    else:
        print("correct")
except ValueError:
    print("invalid input")


