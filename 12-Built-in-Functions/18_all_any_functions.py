# All Any Functions

numbers = list(map(int, input("Enter numbers: ").split()))
print(f"All positive: {all(x > 0 for x in numbers)}")
print(f"Any even: {any(x % 2 == 0 for x in numbers)}")