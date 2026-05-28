# DAY 39
# program 1
diary = input("type a diary entry")
with open("files/diary.txt", "a") as f:
    f.write(diary)

# program 2
with open("files/diary.txt", "r") as f:
    result = f.read()
    print(result)

# program 3
player_name = input("enter a player name")
score = int(input("enter his score"))
with open("files/scores.txt", "a") as f:
    f.write(player_name + ": " + str(score) + "\n")
with open("files/scores.txt", "r") as q:
    result = q.read()
    print(result)

# program 4
try:
    task = input("add a task")
    with open("files/todos.txt", "a") as f:
        f.write(task + "\n")
    with open("files/todos.txt", "r") as q:
        result = q.read()
        print(result)
except FileNotFoundError:
    print("file not found")


# program 5
sentence = input("enter a sentence: ")
with open("files/sentences.txt", "w") as f:
    f.write(sentence + "\n")
words = sentence.split()
print(len(words))



