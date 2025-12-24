# Reading Files - Readlines

filename = input("Enter filename: ")
with open(filename, 'r') as f:
    lines = f.readlines()
    print(lines)