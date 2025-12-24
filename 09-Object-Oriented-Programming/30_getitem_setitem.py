# Getitem Setitem

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

md = MyDict()
key = input("Enter key: ")
value = input("Enter value: ")
md[key] = value
print("Value:", md[key])