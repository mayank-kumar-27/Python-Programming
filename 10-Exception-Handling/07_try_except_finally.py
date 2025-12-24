# Try Except Finally

try:
    file = open(input("Enter filename: "), 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    try:
        file.close()
        print("File closed")
    except NameError:
        pass