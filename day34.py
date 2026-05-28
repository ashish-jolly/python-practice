# DAY 34
# program 1
a = int(input("first number"))
b = int(input("second number"))
op = ("operators (+, -, *, /):")
try:
    result = None
    if op == a + b:
        result = op
    elif op == a - b:
        result = op
    elif op == a * b:
        result = op
    elif op == a / b:
        result = op
    else:
        print("cannot divide by zero")
    print("result:", result)
except ValueError:
    print("invalid input, try again")
