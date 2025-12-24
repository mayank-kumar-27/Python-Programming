# Class Methods

class Math:
    @classmethod
    def square(cls, x):
        return x ** 2

x = int(input("Enter x: "))
print("Square:", Math.square(x))