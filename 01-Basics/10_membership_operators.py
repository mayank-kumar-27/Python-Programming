# Membership Operators

items = input("Enter items separated by space: ").split()
value = input("Enter value: ")
print("value in items:", value in items)
print("value not in items:", value not in items)