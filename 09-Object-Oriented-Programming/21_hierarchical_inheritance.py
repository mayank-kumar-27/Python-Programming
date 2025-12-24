# Hierarchical Inheritance

class Parent:
    def method(self):
        return "Parent"

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
print(c1.method(), c2.method())