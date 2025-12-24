# Set Methods Add Remove

my_set = set(input("Enter initial items separated by space: ").split())
item_add = input("Enter item to add: ")
my_set.add(item_add)
print("After add:", my_set)
item_remove = input("Enter item to remove: ")
if item_remove in my_set:
    my_set.remove(item_remove)
    print("After remove:", my_set)
else:
    print("Item not found")