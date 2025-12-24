# Super Function

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

name = input("Enter name: ")
age = int(input("Enter age: "))
child = Child(name, age)
print(f"Name: {child.name}, Age: {child.age}")