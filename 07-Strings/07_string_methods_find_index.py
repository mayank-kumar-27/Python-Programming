# String Methods Find Index

my_string = input("Enter a string: ")
sub = input("Enter substring: ")
find_pos = my_string.find(sub)
print("Find:", find_pos)
if sub in my_string:
    index_pos = my_string.index(sub)
    print("Index:", index_pos)
else:
    print("Substring not found")