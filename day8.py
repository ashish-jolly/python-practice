# Day 8
# program 1
# for i in range(1, 21):
#     if i % 2 == 0 and i > 5:
#          print(i)

# program 2
# for i in range(1, 21):
#     if i % 3 == 0 or i < 6:
#         print(i)

# program 3
# for i in range(1, 26):
#     if not i % 2 == 0 and i > 10:
#         print(i)

# program 4
# for a in range(1, 31):
#     if a % 2 == 0 or a % 3 == 0:
#         print(a)

# program 5
# for i in range(1, 31):
#     if i % 2 == 0 and not i % 3 == 0:
#         print(i)

# program 6
numbers = [3, 5, 2, 1, 10]
index = 0
max_num = numbers[0]
while index < len(numbers):
    if numbers[index] > max_num:
        max_num = numbers[index]
    index += 1
result = {"largest": max_num}
print(result)

# program 7
numbers = [2, 5, 6, 4, 8]
index == 0
min_num = numbers[0]
while index < len(numbers):
    if numbers[index] < min_num:
        min_num = numbers[index]
    index += 1
result = {"smallest": min_num}
print(result)


