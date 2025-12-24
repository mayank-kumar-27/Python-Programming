# String Immutability

my_string = "Hello"
print("Original:", my_string)
try:
    my_string[0] = "h"
except TypeError as e:
    print("Error:", e)