# DAY 42
# program 1
class student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade
    def introduce(self):
        print(f"my name is {self.name}, i am {self.age}, my grade is {self.grade}")
    def update_grade(self, new_grade):
        self.grade = new_grade
        print(new_grade)
student1 = student("Ashish", 18, "B")
print(student1.name)
print(student1.age)
print(student1.grade)
student1.introduce()
student1.update_grade("A")
student1.introduce()

# program 2
class workout_machine:
    def __init__(self, weight, muscle, age_required_to_use):
        self.weight = weight
        self.muscle = muscle
        self.age_required_to_use = age_required_to_use
    def use_guidance(self):
        print(f"weight is {self.weight}. targeted muscle is {self.muscle}. do not use under {self.age_required_to_use} bodybuilders")
workout_machine1 = workout_machine(250, "leg", 18)
print(workout_machine1.weight)
print(workout_machine1.muscle)
print(workout_machine1.age_required_to_use)
workout_machine1.use_guidance()
class treadmill(workout_machine):
    pass
    def use_guidance(self):
        print(f"weight is {self.weight}. useful for {self.muscle}. do not use under {self.age_required_to_use}")
treadmill1 = treadmill(5, "for endurance and calorie burning", 7)
print(treadmill1.weight)
treadmill1.use_guidance()

# program 3
class electrnic_gadget_TV:
    def __init__(self, gadget_name, company_name, display):
        self.gadget_name = gadget_name
        self.company_name = company_name
        self.display = display
    def product_info(self):
        print(f"Its a high quality {self.gadget_name} built by {self.company_name} and its diplay is {self.display} which is great for a better experience")
electrnic_gadgets1 = electrnic_gadget_TV("TV", "TCL", "Qled")
print(electrnic_gadgets1.gadget_name)
print(electrnic_gadgets1.company_name)
print(electrnic_gadgets1.display)
electrnic_gadgets1.product_info()
class elctronic_gadget_mobile(electrnic_gadget_TV):
    pass
    def product_info(self):
        print(f"its a better quality {self.gadget_name} crafted by {self.company_name} and its display is {self.display} which is great to watch movies")
electrnic_gadgets2 = elctronic_gadget_mobile("mobile", "poco", "amoled")
print(electrnic_gadgets2.gadget_name)
print(electrnic_gadgets2.company_name)
print(electrnic_gadgets2.display)
electrnic_gadgets2.product_info()
              


        