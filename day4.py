# Day 4
# Tuple

# program 1
tuple1 = ("football", "badminton", "basketball")
for x in tuple1:
    print(x)

# program 2
tuple1 = ("cricket", "boxing","kickboxing")
print(len(tuple1))

# program 3
tuple1 = ("boxing", "kickboxing", "racing")
tuple2 = (15, 20, 25, 30)
tuple3 = (tuple1 + tuple2)
print(tuple3)

# program 4
tuple1 = ("boxing", "kickboxing", "racing")
print(tuple1[1])

# program 5
tuple1 = ("boxing", "kickboxing", "racing")
tuple2 = (15, 20, 25, 30)
tuple3 = (tuple1 + tuple2)
print(tuple3[4])

# set
# program 6
set1 = {"boxing", "kickboxing","racing"}
print(set1)

# program 7
set1 = {"boxing", "kickboxing", "racing"}
print(len(set1))

# program 8
set1 = {"boxing", "kickboxing", "racing"}
set1.add ("football")
print(set1)

# program 9
set1 = {"boxing", "kickboxing", "racing"}
set1.update(["badminton", "football", "swimming"])
print(set1)

# program 10
set1 = {"boxing", "kickboxing", "racing"}
set1.remove("kickboxing")
print(set1)

# program 11
set1 = {"boxing", "kickboxing", "racing"}
set1.discard("cricket")
print(set1)

# program 12
set1 = {"cricket", "workout", "jogging"}
set2 = (1, 2, 3, 4)
set3 = set1.union(set2)
print(set3)

# program 13
set1 = {"rehab", "workout", "jogging"}
set1.clear()
print(set1)

# Day 4 - modified version of day 3 program 17
# program 14
list1 = ["Laptop", "Mouse", "Charger"]
set1 = {"rehab", "workout", "jogging"}
list1.append("boxing")
list1.insert(0, "keyboard")
set1.update(["reading", "meditation"])
set1.remove("jogging")
print(list1)
print(set1)

# program 15
list = ["apple", "banana", "apple", "milk", "banana", "egg"]
list.append("bread")
list.insert(1, "water")
list.remove("milk")
print(list)

# program 16
list = ["pen", "book", "phone"]
list.append("laptop")
list.insert(1, "tablet")
list.remove("phone")
print(list)

# program 17
tuple = ("red", "blue", "green", "yellow") 
print("red")
print("yellow")
print(len(tuple))

# program 18
set = {"football", "cricket", "tennis"}
set.add("badminton")
set.add("hockey")
set.remove("tennis")
print(set)

# program 19
numbers = [5, 10, 15, 20]
print(5)
print(15)
print(20)

# program 20 - operators
a = 10
b = 10
print(a !=b)

score = 10
score += 20
print(score)

print(2 ** 3)
print(3 ** 2)
print(5 ** 2)

x = 5
x +=3
print(x != 10)

a = 10
b = 5
print(a == b)

score = 50
score -= 10
print(score)

num = 4
num *= 3
print(num)

x = 5
x += 5
print(x == 10)

a = 8
b = 3
a += b
print(a)