# List Enumerate

my_list = input("Enter list separated by space: ").split()
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")