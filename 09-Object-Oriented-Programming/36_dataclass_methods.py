# Dataclass Methods

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def distance(self):
        return (self.x**2 + self.y**2)**0.5

x = int(input("Enter x: "))
y = int(input("Enter y: "))
p = Point(x, y)
print(f"Distance: {p.distance()}")