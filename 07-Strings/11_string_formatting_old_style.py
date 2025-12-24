# String Formatting Old Style

name = input("Enter name: ")
age = int(input("Enter age: "))
formatted = "Hello %s, you are %d years old." % (name, age)
print("Formatted:", formatted)