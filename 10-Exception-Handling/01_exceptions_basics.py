# Exceptions Basics

# Exceptions are errors that occur during execution
try:
    x = int(input("Enter a number: "))
    print(f"You entered: {x}")
except ValueError:
    print("That's not a valid number!")