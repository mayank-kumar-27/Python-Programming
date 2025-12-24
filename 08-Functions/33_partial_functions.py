# Partial Functions

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
x = int(input("Enter x: "))
print("Double:", double(x))