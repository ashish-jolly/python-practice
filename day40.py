# DAY 40
# program 1
import math
print(math.sqrt(25))

# program 2
import random
print(random.randint(1, 10))

# program 3
import datetime
print(datetime.date.today())

# program 4
import math
number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
print(math.pow(number1, number2))
print(number1 ** number2)

# program 5
from random import randint
print(randint(1, 100))

# program 6
import datetime
date_time = input("do you want to know today's date")
if date_time == "yes":
    print(datetime.date.today())
else:
    print("comeback when you want to know")
import random, math
game = input("do you want to play a game")
if game == "ok":
    print(random.randint(1, 1000))
else:
    print("okay, next time")
finding_sqrt = input("do you want to find a square root")
if finding_sqrt == "yes":
    number_sqrt = int(input("enter a number"))
    print(math.sqrt(number_sqrt))
else:
    print("when you need to find comeback")

# program 7
result = []
for i in range(5):
    names = input("enter 5 names")
    result.append(names)
print(i)
