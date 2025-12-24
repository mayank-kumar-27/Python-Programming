# Class Variables

class Employee:
    company = "ABC Corp"  # class variable

    def __init__(self, name):
        self.name = name

name = input("Enter employee name: ")
emp = Employee(name)
print(f"Name: {emp.name}, Company: {Employee.company}")