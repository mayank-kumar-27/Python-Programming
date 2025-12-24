# List Methods Count Index

my_list = input("Enter list separated by space: ").split()
item = input("Enter item to count/index: ")
count = my_list.count(item)
print("Count:", count)
if item in my_list:
    index = my_list.index(item)
    print("Index:", index)
else:
    print("Item not found")