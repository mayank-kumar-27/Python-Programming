# Deleters

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name

person = Person("John")
print("Name:", person.name)
del person.name
print("Name deleted")