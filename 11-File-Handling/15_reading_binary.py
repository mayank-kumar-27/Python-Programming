# Reading Binary

filename = input("Enter filename: ")
with open(filename, 'rb') as f:
    data = f.read()
    print(data)