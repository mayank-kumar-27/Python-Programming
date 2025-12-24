# Positional Arguments

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
print("Division:", divide(a, b))