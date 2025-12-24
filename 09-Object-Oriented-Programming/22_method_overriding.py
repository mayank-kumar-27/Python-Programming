# Method Overriding

class Parent:
    def greet(self):
        return "Hello from parent"

class Child(Parent):
    def greet(self):
        return "Hello from child"

child = Child()
print(child.greet())