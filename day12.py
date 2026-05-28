# DAY 12
# dictionary in depth
# program 1
dict1 = {"name": "Ashish", "age": 17, "city": "Kochi", "goal": "Top level backend engineer"}
print(dict1["name"])
dict1["days_coding"] = 12
dict1["age"] = 18
for keys in dict1:
    print(keys, dict1[keys])
if "goal" in dict1:
    print("found")

# program 2
def create_profile(**kwargs):
    return kwargs
print (create_profile(name="Ashish", age=17, city="Kochi", goal="Top level backend engineer"))

# program 3
tuple1 = ("bottle", "flask", "TV", "glass")
print(tuple1[2])

# program 4
sets1 = {"bottle", "bottle", "flask", "TV", "flask"}
print(sets1)

# program 5
def Unique_items(*args):
    return set(args)
print(Unique_items("boxing", "workout", "podcast", "podcast", "boxing", "reading"))

def item_info(items = ("rehab", "journaling", "jogging", "sunlight", "jogging")):
    return {"total":len(items), "unique": Unique_items(*items)}
print(item_info(("rehab", "journaling", "jogging","sunlight")))

# program 6
def count_words (sentence):
    words = sentence.split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
print(count_words("workout rehab rehab workout workout reading"))

# program 7
def group_by_length(*args):
    result = {}
    for word in args:
        if len(word) in result:
            result[len(word)].append(word)
        else:
            result[len(word)] = [word]
    return result
print(group_by_length("pen", "pencil", "rubber", "cap", "phone"))
