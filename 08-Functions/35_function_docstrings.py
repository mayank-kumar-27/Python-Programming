# Function Docstrings

def greet(name):
    """This function greets the user."""
    return f"Hello {name}"

name = input("Enter name: ")
print(greet(name))
print("Docstring:", greet.__doc__)