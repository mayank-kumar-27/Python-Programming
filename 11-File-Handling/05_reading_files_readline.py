# Reading Files - Readline

filename = input("Enter filename: ")
with open(filename, 'r') as f:
    line = f.readline()
    print(line)