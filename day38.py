# DAY 38
# program 1
with open("notes.txt", "a") as f:
    f.write("\nsecond line")

# program 2
with open("notes.txt", "r") as f:
    result = f.read()
    print(result)