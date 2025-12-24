# List Copy Shallow Deep

import copy
my_list = input("Enter list separated by space: ").split()
shallow_copy = my_list.copy()
deep_copy = copy.deepcopy(my_list)
print("Original:", my_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)