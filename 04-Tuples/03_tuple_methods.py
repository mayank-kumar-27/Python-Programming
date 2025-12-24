# Tuple Methods

items = input("Enter items separated by space: ").split()
my_tuple = tuple(items)
item = input("Enter item to count/index: ")
count = my_tuple.count(item)
print("Count:", count)
if item in my_tuple:
    index = my_tuple.index(item)
    print("Index:", index)
else:
    print("Item not found")