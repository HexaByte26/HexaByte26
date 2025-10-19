array = [("ABC", 10), ("DEF", 5), ("GHI", 1)]
sorted_arr = sorted(array, key=lambda arr: arr[1])
print(sorted_arr)

class Vehicle:
    def __init__(self, name, hp, torque):
        self.name = name
        self.hp = hp
        self.torque = torque
    
    def __repr__(self):
        return f"{(self.name, self.hp, self.torque)}"
    
car1 = Vehicle("toyota", 150, 25)
car2 = Vehicle("nissan", 115, 55)

cars = [car1, car2]

sorted_cars = sorted(cars, key=lambda car: car.torque, reverse=True)
print(sorted_cars)

class Student:
    def __init__(self, name, age, gender, heigth, weight, bmi):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = heigth
        self.weight = weight
        self.bmi = bmi

    def __repr__(self):
        return f"{(self.name, self.age, self.gender, self.height, self.weight, self.bmi)}"
    
student1 = Student('vincent', 15, "male", 151, 50, 20.1)
student2 = Student('miguel', 25, "male", 175, 67, 22.5)
student3 = Student('sarah', 17, "female", 145, 45, 19.1)

students = [student1, student2, student3]

sorted_students = sorted(students, key=lambda student: student.bmi)
for student in sorted_students:
    print(student)