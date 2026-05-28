# DAY 20
# CONSOLIDATING WHAT I LEARNED MORE DEEPLY
# program 1
dict1 = {"alen": "56", "neymar": "47", "ronaldo": "71"}
for key in dict1:
    print(key, dict1[key])

# program 2
prices = {"apple": 30, "laptop": 80000, "pen": 10, "phone": 25000, "book": 45}
for key in prices:
    if prices[key] > 50:
        print(key, prices[key])

# program 3
students = {"alen": 56, "neymar": 87, "ronaldo": 71, "messi": 92, "mbappe": 78}
top_student = students["alen"]
largest = students["alen"]
for key in students:
    if students[key] > largest:
        largest = students[key]
        top_student = key
print(top_student, largest)

# program 4
inventory = {"apples": 50, "bananas": 30, "oranges": 20, "grapes": 45}
total = 0
for key in inventory:
    total += inventory[key]
print(total)

# program 5
students = {"alen": 56, "neymar": 87, "ronaldo": 71, "messi": 92, "mbappe": 63}
students2 = {}
for key in students:
    if students[key] > 70:
        students2[key] = students[key]
print(students2)

# program 6
prices = {"apple": 100, "laptop": 80000, "pen": 20, "phone": 25000}
for key in prices:
    prices[key] = prices[key] * 0.90
    print(key, prices[key])