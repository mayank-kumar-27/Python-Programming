# String Indexing Slicing

my_string = input("Enter a string: ")
index = int(input("Enter index: "))
if 0 <= index < len(my_string):
    print("Character at index:", my_string[index])
else:
    print("Invalid index")
start = int(input("Enter start: "))
end = int(input("Enter end: "))
print("Slice:", my_string[start:end])