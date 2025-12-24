# Default Arguments

def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

name = input("Enter name: ")
greeting = input("Enter greeting (optional): ")
if greeting:
    print(greet(name, greeting))
else:
    print(greet(name))