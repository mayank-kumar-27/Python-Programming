# Nested Try Except

try:
    x = int(input("Enter x: "))
    try:
        y = int(input("Enter y: "))
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Inner: Division by zero")
except ValueError:
    print("Outer: Invalid input")