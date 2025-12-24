# Nested If

age = int(input("Enter age: "))
if age >= 18:
    has_id = input("Do you have ID? (yes/no): ").lower()
    if has_id == "yes":
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Too young")