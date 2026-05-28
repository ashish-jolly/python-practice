# program 1
a = 15
b = 15
print(a == b)

# program 2
a = 18
b = 19
print(a != b)
      
# program 3
a = 10
b = 15
print(a < b)
a = 10
b = 15
print(a > b)

# program 4
a = 20
b = 15
print(a >= b) , print(a <= b)

# program 5
a = 15
print(a == 15 and a < 20)

# program 6
a = 18
print(a == 18 or a > 19)

# program 7
a = 18
print(not(a == 18))

# program 8
text = """
my name is ashish. i coming from panangad.
 in my house i have father,mother,brother. my hobbies are playing badminton,football.
"""
print(text)

# program 9
text = "hp 15"
print(text[3])

# program 10
text = "self improvement"
print(text[1:6])

# program 11
text = "self improvement"
print(len(text))

# program 12
text = "   self improvement   "
print(text.strip())

# program 13
text = "SELF IMPROVEMENT"
print(text.lower())
text = "self improvement"
print(text.upper())

# program 14
text = "self improvement"
print(text.replace("i","e"))

# program 15
a = "master "
b = "javascript"
d = " with great skill"
c = a + b + d
print(c)

# program 16
name = "Ashish"
skill = "programmer"
text = "I am {} and I am a {}"
print(text.format(name, skill))

# program 17 
#list
list1 = ["Laptop", "mouse", "charger"]
print(len(list1))
list1 = ["Laptop", "Mouse", "Charger"]
print(list1[2])

# program 18
list2 = [50, 100, 150, 200]
sum = list2[0] + list2[2]
print(sum)

# program 19
list1 = ["Laptop", "Mouse", "Charger"]
list1[1] = "Keyboard"
print(list1)

# program 20
list1 = ["Laptop", "Mouse", "Charger"]

print(list1)
for x in list1:
    print(x)

# program 21
item = ["Laptop", "Mouse", "Charger"]
item.append ("Keyboard")
print(item)

# program 22
item = ["Laptop", "Mouse", "Charger"]
item.insert (0, "keyboard")
item.append("Bag")
print(item)

# program 23
item = ["TV", "Laptop", "refrigerator",]
item.remove ("refrigerator")
print(item)

# program 24
item = ["TV", "Laptop", "Dumbbell"]
item.clear()
print(item)

# program 25
item = ["TV", "Laptop", "Dumbbell"]
del item
print(item)
