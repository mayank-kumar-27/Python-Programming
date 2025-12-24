# Instance Methods

class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Sum:", calc.add(a, b))