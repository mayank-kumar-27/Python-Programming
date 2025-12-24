# File Truncate

filename = input("Enter filename: ")
with open(filename, 'w') as f:
    f.write("Hello World")
    f.truncate(5)
print("File truncated")