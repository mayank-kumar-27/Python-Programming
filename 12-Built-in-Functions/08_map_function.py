# Map Function

numbers = list(map(int, input("Enter numbers: ").split()))
squares = list(map(lambda x: x**2, numbers))
print(f"Squares: {squares}")