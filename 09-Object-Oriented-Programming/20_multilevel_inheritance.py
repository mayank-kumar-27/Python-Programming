# Multilevel Inheritance

class Grandparent:
    def method(self):
        return "Grandparent"

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

child = Child()
print(child.method())