# Dict Methods Update Pop

my_dict = {'a': 1, 'b': 2}
update_dict = {'c': 3, 'd': 4}
my_dict.update(update_dict)
print("After update:", my_dict)
key_pop = input("Enter key to pop: ")
if key_pop in my_dict:
    popped = my_dict.pop(key_pop)
    print("Popped:", popped)
    print("Dict:", my_dict)
else:
    print("Key not found")