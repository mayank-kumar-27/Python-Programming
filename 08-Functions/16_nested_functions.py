# Nested Functions

def outer(x):
    def inner(y):
        return x + y
    return inner

x = int(input("Enter x: "))
y = int(input("Enter y: "))
result = outer(x)(y)
print("Result:", result)