# Raise From

try:
    x = int(input("Enter number: "))
    if x < 0:
        raise ValueError("Negative number") from None
except ValueError as e:
    print(f"Error: {e}")