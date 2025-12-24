# List Methods Insert Remove

my_list = input("Enter list separated by space: ").split()
index = int(input("Enter index to insert: "))
item = input("Enter item to insert: ")
my_list.insert(index, item)
print("After insert:", my_list)
item_remove = input("Enter item to remove: ")
if item_remove in my_list:
    my_list.remove(item_remove)
    print("After remove:", my_list)
else:
    print("Item not found")