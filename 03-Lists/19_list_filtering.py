# List Filtering

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)