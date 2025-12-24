# Dict Adding Removing

my_dict = {'a': 1, 'b': 2}
key_add = input("Enter key to add: ")
value_add = input("Enter value: ")
my_dict[key_add] = value_add
print("After add:", my_dict)
key_remove = input("Enter key to remove: ")
if key_remove in my_dict:
    del my_dict[key_remove]
    print("After remove:", my_dict)
else:
    print("Key not found")