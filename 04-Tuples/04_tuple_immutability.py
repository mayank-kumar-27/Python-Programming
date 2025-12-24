# Tuple Immutability

my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)
try:
    my_tuple[0] = 4
except TypeError as e:
    print("Error:", e)