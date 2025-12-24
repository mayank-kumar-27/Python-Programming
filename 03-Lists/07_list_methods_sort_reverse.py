# List Methods Sort Reverse

my_list = input("Enter numbers separated by space: ").split()
my_list = [int(x) for x in my_list]
my_list.sort()
print("Sorted:", my_list)
my_list.reverse()
print("Reversed:", my_list)