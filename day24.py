# DAY 24
# CONSOLIDATING WHATR I LEARNED MORE DEEPLY
# program 1
sentence = "hello world python"
words = sentence.split()
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
print(" ".join(reversed_words))

# program 2
numbers = [1, 2, 3, 2, 1, 4, 3, 5]
result = {}
for number in numbers:
    result[number] = 1
print(list(result.keys()))

    

