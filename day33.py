# DAY 32
# program 1
try:
    number = int(input("enter a number"))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print("cannot divided by zero")
except ValueError:
    print("cannot proceed letter")
finally:
    print("program finished")

# program 2
try:
    number = int(input("enter a number"))
    if number < 0:
        print("cannot square root a negative number")
    else:
        result = number ** 0.5
        print(result)
except ValueError:
    print("invalid input")
finally:
    print("calculation finished")
