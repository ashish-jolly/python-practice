# Day 5
# Dictionary
# program 1
dict1 = {
    "name : ashish",
    "email : ashish@gmail.com",
    "phone : 123456789"
}
print(dict1)

# program 2
dict1 = {
    "workout : body",
    "rehab : shoulder",
    "podcast : mindset"
}
print("podcast")

# program 3
dict1 = {
    "podcast" : "mindset",
    "workout" : "mindset and body",
    "rehab" : "shoulder"
 }
a = dict1.get("rehab")
print(a)

# program 4
dict1 = {
    "workout" :"mindset and body",
    "podcast" : "mindset",
    "rehab" : "shoulder stability"
}
dict1["rehab"] = "shoulder rehab"
print(dict1)

# program 5
dict1 ={
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "shoulder rehab" : "shoulder stability"
}
for x in dict1:
    print(x)

# program 5
dict1 = {
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "rehab" : "shoulder stability"
}
for x in dict1:
    print(dict1[x])

# program 6
dict1 = {
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "rehab" : "shoulder stability"
}
for x, y in dict1.items():
    print (x, y)

# program 7
dict1 = {
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "rehab" : "shoulder stability"
}
print(len(dict1))

# program 8
dict1 = {
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "rehab" : "shoulder stability"
}
dict1["reading"] = "knowledge and mental toughness"
print(dict1)

# program 9
dict1 = {
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "rehab" : "shoulder stability"
}
dict1.pop("rehab")
print(dict1)

# program 10
dict1 = {
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "rehab" : "shoulder stability"
}
del dict1["rehab"]
print(dict1)

# program 11
dict1 = {
    "workout" : "mindset and body",
    "podcast" : "mindset",
    "reading" : "knowledge"
}
dict1.clear()
print(dict1)

# IF Else
# program 12
x = 10
if x > 5:
    print("it is a positive number")

# program 13
y = -10
if y > 0:
    print("it is a positive number")
elif y < 0:
    print("it is a negative number")

# program 14
a = -3
if a > 0:
    print("it is a positive number")
elif a < 0:
    print("it is a negative number")
else:
    print("it is a ZERO")
    
# program 15
a = -1
if a >= 0:
    if a > 0:
        print("it is a positive number")
    else: 
        print("it is a zero")
else:
    print("it is a negative number")

# program 16
a = 10
if a > 5 and a < 20:
    print("hello")

# While loop
# program 17
i = 1
while i < 10:
    print(i)
    i += 1

# program 18
i = 1
x = "QUICK HEAL"
while i < 11:
    print(x)
    i += 1

# program 19
a = 1
while a < 11:
    print(a)
    a += 1

# program 20
x = 10
while x > 0:
    print(x)
    x -= 1

# program 21
n = 2
while n < 22:
    print(n)
    n += 2

# program 22
n = 20
while n > 0:
    print(n)
    n -= 2

# program 23
list = [2, 7, 3, 10, 5, 8]
while list > 9:
    print(list)
    list = 1
    
    

 

    