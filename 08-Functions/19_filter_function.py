# Filter Function

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)