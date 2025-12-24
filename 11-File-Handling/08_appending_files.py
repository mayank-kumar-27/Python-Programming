# Appending Files

filename = input("Enter filename: ")
text = input("Enter text to append: ")
with open(filename, 'a') as f:
    f.write(text + '\n')
print("Text appended to file")