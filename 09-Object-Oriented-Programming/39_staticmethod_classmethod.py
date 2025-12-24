# Staticmethod and Classmethod

class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def from_string(cls, s):
        a, b = map(int, s.split('+'))
        return cls.add(a, b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"Sum: {Math.add(a, b)}")

s = input("Enter expression like 1+2: ")
print(f"Sum: {Math.from_string(s)}")