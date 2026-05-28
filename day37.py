# DAY 37
# program 1
item1 = 500
item2 = 300
item3 = 200
total = 0
try:
    q1 = (int(input("how many of item1")))
    q2 = (int(input("how many of item2")))
    q3 = int(input("how many of item3"))
    total = (item1 * q1) + (item2 * q2) + (item3 * q3)
    if total > 800:
        print("discount:", total - total * 0.10)
    else:
        print(total)
except ValueError:
    print("invalid input")

# program 2
password = input("enter a password")
pass_length = len(password)
if pass_length < 6:
    print("too short")
elif pass_length >= 6 and pass_length <= 9:
    print("weak")
elif pass_length >= 10:
    print("strong")

# program 3
point = 0
q1 = input("what is football\n")
if q1 == "football is a sport":
    point += 1
else:
    point = 0
q2 = input("how to be mentally tough\n")
if q2 == "when you do things when you dont want to":
    point += 1
else:
    point = 0
q3 = input("what is programming\n")
if q3 == "its a skill":
    point += 1
else:
    point = 0
print(point)








        
