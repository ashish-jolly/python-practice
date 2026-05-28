# DAT 23
# CONSOLIDATING WHAT I LEARNED MORE DEEPLY
# program 1
dict1 = {"apple": 5, "banana": 3, "cherry": 8}
dict2 = {"banana": 2, "cherry": 1, "date": 4}
result = {}
for key in dict1:
    if key in dict2:
        result[key] = dict1[key] + dict2[key]
    else:
         result[key] = dict1[key]
for key in dict2:
    if key not in result:
        result[key] = dict2[key]
print(result)

# program 2
sentence = "hello world python"
word = sentence.split()
reversed_words = []
for letter in word:
    if reversed_words("".join(list)):
        reversed_words.append(word[:: -1])
print(reversed_words)