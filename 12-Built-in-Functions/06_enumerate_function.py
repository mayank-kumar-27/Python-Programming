# Enumerate Function

items = input("Enter items separated by space: ").split()
for index, item in enumerate(items):
    print(f"{index}: {item}")