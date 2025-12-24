# Reading Files - Read

filename = input("Enter filename: ")
with open(filename, 'r') as f:
    content = f.read()
    print(content)