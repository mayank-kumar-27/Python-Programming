# Multiple Inheritance

class A:
    def method_a(self):
        return "A"

class B:
    def method_b(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.method_a(), c.method_b())