# Zip Function

list1 = input("Enter first list: ").split()
list2 = input("Enter second list: ").split()
for a, b in zip(list1, list2):
    print(f"{a} - {b}")