# Self Parameter

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

radius = float(input("Enter radius: "))
circle = Circle(radius)
print("Area:", circle.area())