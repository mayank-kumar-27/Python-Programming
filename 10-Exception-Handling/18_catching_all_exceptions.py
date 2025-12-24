# Catching All Exceptions

try:
    x = int(input("Enter number: "))
    result = 10 / x
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")