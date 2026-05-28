# DAY 41
# program 1
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, i got {self.grade} grade")
student1 = student("Ali", 20, "A")
print(student1.name)
print(student1.age)
print(student1.grade)
student1.introduce()