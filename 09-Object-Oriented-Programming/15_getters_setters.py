# Getters Setters

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

person = Person("John")
print("Name:", person.name)
new_name = input("Enter new name: ")
person.name = new_name
print("Updated name:", person.name)