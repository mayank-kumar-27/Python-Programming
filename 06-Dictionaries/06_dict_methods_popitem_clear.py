# Dict Methods Popitem Clear

my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_item = my_dict.popitem()
print("Popped item:", popped_item)
print("Dict:", my_dict)
choice = input("Clear dict? (yes/no): ").lower()
if choice == "yes":
    my_dict.clear()
    print("Dict cleared:", my_dict)