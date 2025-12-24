# Private Attributes

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

name = input("Enter name: ")
person = Person(name)
print("Name:", person.get_name())