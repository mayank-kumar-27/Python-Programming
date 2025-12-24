# Tuple Membership

my_tuple = tuple(input("Enter items separated by space: ").split())
item = input("Enter item to check: ")
print("In tuple:", item in my_tuple)
print("Not in tuple:", item not in my_tuple)