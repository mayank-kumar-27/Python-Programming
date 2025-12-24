# Open Function

file = open(input("Enter filename: "), 'r')
content = file.read()
print(content)
file.close()