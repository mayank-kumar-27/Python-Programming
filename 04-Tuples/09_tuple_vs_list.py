# Tuple Vs List

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
print("List:", my_list, "Type:", type(my_list))
print("Tuple:", my_tuple, "Type:", type(my_tuple))
# Try to modify
my_list[0] = 4
print("Modified list:", my_list)
try:
    my_tuple[0] = 4
except TypeError as e:
    print("Tuple error:", e)