# Catching Specific Exceptions

try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Division by zero!")
except ValueError:
    print("Invalid input!")