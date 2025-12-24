# Dict Methods Get Setdefault

my_dict = {'a': 1, 'b': 2}
key = input("Enter key: ")
value = my_dict.get(key, "Not found")
print("Get:", value)
default_value = my_dict.setdefault(key, 0)
print("Setdefault:", default_value)
print("Dict:", my_dict)