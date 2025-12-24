# List Indexing

items = input("Enter items separated by space: ").split()
index = int(input("Enter index: "))
if 0 <= index < len(items):
    print("Item at index:", items[index])
else:
    print("Invalid index")