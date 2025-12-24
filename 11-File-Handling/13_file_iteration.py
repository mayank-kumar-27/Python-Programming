# File Iteration

filename = input("Enter filename: ")
with open(filename, 'r') as f:
    for line in f:
        print(line.strip())