# Keyword Arguments

def greet(name, age):
    return f"Hello {name}, you are {age} years old."

name = input("Enter name: ")
age = int(input("Enter age: "))
print(greet(name=name, age=age))