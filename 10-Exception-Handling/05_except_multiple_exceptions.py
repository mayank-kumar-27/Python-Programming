# Except Multiple Exceptions

try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    result = x / y
    print(f"Result: {result}")
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")