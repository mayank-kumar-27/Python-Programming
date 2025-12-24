# File Basics

# Files are used to store data permanently
filename = input("Enter filename: ")
with open(filename, 'w') as f:
    f.write("Hello World")
print("File created")