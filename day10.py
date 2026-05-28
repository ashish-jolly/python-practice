# Day10
# *args, **kwargs
# program 1
def add_numbers (*args):
    return sum(args) 
print(add_numbers(4, 6))
print(add_numbers(3, 3, 3))
print(add_numbers(25, 50, 25))

# program 2
def self_improvement_info (**kwargs):
    return (kwargs)
print(self_improvement_info(workout = "body and mindset", podcast = "mindset", meditation = "mw=ental clarity"))

# program 3
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
subject = ["physics", "chemistry"]
info = {"name": "Ashish", "age" : 17}
student_info(*subject, **info)

# program 4
def get_stats(*args):
    return {"largest": max(args), "smallest": min(args), "total": sum(args)}
print(get_stats(5, 7, 2, 9, 6))

# program 5
def is_even(number):
    return number % 2 == 0
print(is_even(7))

result = [2, 5, 4, 7, 8, 6]
def filter_evens(*args):
    for args in range:
        if is_even % 2 == 0:
            result.append
            return result
        print(result)



              