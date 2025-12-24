# String Alignment

my_string = input("Enter a string: ")
width = int(input("Enter width: "))
print("Left:", my_string.ljust(width))
print("Center:", my_string.center(width))
print("Right:", my_string.rjust(width))