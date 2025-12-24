# Method Overloading Simulation

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print("Sum:", calc.add(a, b, c))