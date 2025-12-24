# Set Methods Update Discard

my_set = set(input("Enter initial items separated by space: ").split())
items_update = input("Enter items to update separated by space: ").split()
my_set.update(items_update)
print("After update:", my_set)
item_discard = input("Enter item to discard: ")
my_set.discard(item_discard)
print("After discard:", my_set)