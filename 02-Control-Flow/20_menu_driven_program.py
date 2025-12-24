# Menu Driven Program

print("1. Add\n2. Subtract")
choice = int(input("Enter choice: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)