# Dict Accessing Values

my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter key: ")
if key in my_dict:
    print("Value:", my_dict[key])
else:
    print("Key not found")