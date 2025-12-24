# Tuple Indexing Slicing

items = input("Enter items separated by space: ").split()
my_tuple = tuple(items)
index = int(input("Enter index: "))
if 0 <= index < len(my_tuple):
    print("Item at index:", my_tuple[index])
else:
    print("Invalid index")
start = int(input("Enter start: "))
end = int(input("Enter end: "))
print("Slice:", my_tuple[start:end])