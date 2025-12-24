# Assertion Error

try:
    x = int(input("Enter positive number: "))
    assert x > 0, "Number must be positive"
    print(f"Number: {x}")
except AssertionError as e:
    print(f"Assertion failed: {e}")