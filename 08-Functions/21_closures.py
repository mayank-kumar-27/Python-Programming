# Closures

def outer(x):
    def inner(y):
        return x + y
    return inner

x = int(input("Enter x: "))
closure = outer(x)
y = int(input("Enter y: "))
print("Result:", closure(y))