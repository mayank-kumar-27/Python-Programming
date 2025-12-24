# Property Decorator

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

r = float(input("Enter radius: "))
c = Circle(r)
print(f"Radius: {c.radius}")