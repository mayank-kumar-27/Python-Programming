# Higher Order Functions

def apply_func(func, x):
    return func(x)

x = int(input("Enter x: "))
result = apply_func(lambda y: y**2, x)
print("Square:", result)