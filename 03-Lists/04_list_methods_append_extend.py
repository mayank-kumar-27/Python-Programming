# List Methods Append Extend

my_list = input("Enter initial list separated by space: ").split()
item = input("Enter item to append: ")
my_list.append(item)
print("After append:", my_list)
more_items = input("Enter items to extend separated by space: ").split()
my_list.extend(more_items)
print("After extend:", my_list)