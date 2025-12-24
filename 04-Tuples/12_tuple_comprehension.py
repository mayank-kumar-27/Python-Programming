# Tuple Comprehension

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
squares = tuple(x**2 for x in numbers)
print("Squares tuple:", squares)