# Set Membership

my_set = set(input("Enter items separated by space: ").split())
item = input("Enter item to check: ")
print("In set:", item in my_set)
print("Not in set:", item not in my_set)