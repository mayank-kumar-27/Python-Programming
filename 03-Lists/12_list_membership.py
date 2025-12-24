# List Membership

my_list = input("Enter list separated by space: ").split()
item = input("Enter item to check: ")
print("In list:", item in my_list)
print("Not in list:", item not in my_list)