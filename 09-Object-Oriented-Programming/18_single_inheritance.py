# Single Inheritance

class Parent:
    def greet(self):
        return "Hello from parent"

class Child(Parent):
    pass

child = Child()
print(child.greet())