# Kwargs Parameter

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

name = input("Enter name: ")
age = input("Enter age: ")
print_kwargs(name=name, age=age)