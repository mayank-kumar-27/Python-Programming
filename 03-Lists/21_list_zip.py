# List Zip

list1 = input("Enter first list separated by space: ").split()
list2 = input("Enter second list separated by space: ").split()
zipped = list(zip(list1, list2))
print("Zipped:", zipped)