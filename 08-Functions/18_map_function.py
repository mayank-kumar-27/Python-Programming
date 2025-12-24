# Map Function

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)