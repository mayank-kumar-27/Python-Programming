# Writing Files

filename = input("Enter filename: ")
text = input("Enter text to write: ")
with open(filename, 'w') as f:
    f.write(text)
print("Text written to file")