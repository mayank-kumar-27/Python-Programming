# Binary Files

filename = input("Enter filename: ")
with open(filename, 'wb') as f:
    f.write(b"Hello World")
print("Binary data written")