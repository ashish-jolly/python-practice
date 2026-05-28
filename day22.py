# DAY 22
# CONSOLIDATING WHAT I LEARNED DEEPLY
# program 1
word_counts = {"apple": 3, "banana": 2, "cherry": 5, "date": 1, "elderberry": 4}
most_frequent_word = "apple"
highest_count = word_counts["apple"]
for word in word_counts:
    if word_counts[word] > highest_count:
        highest_count = word_counts[word]
        most_frequent_word = word
print(most_frequent_word, highest_count)

# program 2
numbers = [1, 2, 3, 4, 5]
dict1 = {}
for number in numbers:
    dict1[number] = number ** 2
print(dict1)

# program 3
students = {"alen": 45, "neymar": 78, "ronaldo": 50, "messi": 32, "mbappe": 91}
for key in students:
    if students[key] >= 50:
        print(key, "pass")
    else:
        print(key, "fail")

# program 4
shop = {"apple": 30, "laptop": 80000, "pen": 10, "phone": 25000, "book": 200}
total = 0
most_expensive_item = "apple"
highest_price = shop["apple"]
for key in shop:
    total += shop[key]
    if shop[key] > highest_price:
        highest_price = shop[key]
        most_expensive_item = key
print(total)
print(most_expensive_item)

# program 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
dict1 = {"even": [], "odd": []}
for number in numbers:
    if number % 2 == 0:
        dict1["even"].append(number)
    else:
        dict1["odd"].append(number)
print(dict1)
