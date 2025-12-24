# Init Constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter name: ")
age = int(input("Enter age: "))
student = Student(name, age)
print(f"Name: {student.name}, Age: {student.age}")