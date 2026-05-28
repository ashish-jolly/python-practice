# Day 9 Functions
# program 1
def hello_func():
    pass

print(hello_func)

# program 2
def hello_func():
    print ("hello_func!")
hello_func()

# program 3
def hello_func():
    print ("hello_func.")

hello_func()
hello_func()
hello_func()
hello_func()

# program 4
def hello_func():
    return "hello_func!"
print(hello_func())

# program 5
def hello_func():
    return 'Hello_Function.'

print(hello_func().upper())

# program 6
def hello_func(greeting):
    return "{}function".format(greeting)
print(hello_func("Hi "))

# program 7
def hello_func(greeting, name = "You"):
    return "{}, {}".format(greeting, name)
print(hello_func ("Hi ", name = "Ashish"))

# program 8
def student_info(name, grade):
    return "{} is in grade {}" .format(name, grade)
print(student_info("john", grade = 10))

# program 9
def add_numbers(a, b):
    return a + b
print(add_numbers(8, 5))
print(add_numbers(2, 5))
print(add_numbers(5, 4))

# program 10
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info("computer science", "programmer", name="Ashish", age=17)

# program 11
def add_numbers(*args (a, b, c, d)):
    return [a + b + c + d]
print(add_number9(8, 4, 5, 6))








