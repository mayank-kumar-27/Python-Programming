# Len Method

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

items = input("Enter items separated by space: ").split()
my_list = MyList(items)
print("Length:", len(my_list))