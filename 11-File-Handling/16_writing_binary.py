# Writing Binary

filename = input("Enter filename: ")
data = bytes(input("Enter data: "), 'utf-8')
with open(filename, 'wb') as f:
    f.write(data)
print("Binary data written")