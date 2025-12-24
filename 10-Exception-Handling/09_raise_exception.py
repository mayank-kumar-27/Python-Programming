# Raise Exception

age = int(input("Enter age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
print(f"Age: {age}")