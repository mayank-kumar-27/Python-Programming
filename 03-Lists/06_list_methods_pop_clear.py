# List Methods Pop Clear

my_list = input("Enter list separated by space: ").split()
index = int(input("Enter index to pop: "))
if 0 <= index < len(my_list):
    popped = my_list.pop(index)
    print("Popped:", popped)
    print("List after pop:", my_list)
else:
    print("Invalid index")
choice = input("Clear list? (yes/no): ").lower()
if choice == "yes":
    my_list.clear()
    print("List cleared:", my_list)