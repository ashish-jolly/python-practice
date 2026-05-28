# Day 6
# Loops=If/Else(warmup)
# program 1
a = 1
while a <= 20:
    if a % 3 == 0:
        print(a)
    a += 1

# program 2
a = 10
while a >= 1:
    print(a)
    a -= 1

# program 3 
a = 1
while a <= 15:
    if a % 5 == 0:
       print("Fizz")
    else:
        print(a)
    a += 1

# program 4
list = [4, 7, 2, 9, 10]
index = 0
counter = 0
while index < len(list):
    if list[index] > 5:
        counter += 1
    index += 1
print(counter)
        

    
    
    
        
    

    
    
