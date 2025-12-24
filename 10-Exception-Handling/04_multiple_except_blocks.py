# Multiple Except Blocks

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number")
except Exception as e:
    print(f"An error occurred: {e}")