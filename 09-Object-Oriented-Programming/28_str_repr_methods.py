# Str Repr Methods

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person('{self.name}')"

p = Person("John")
print(str(p))
print(repr(p))