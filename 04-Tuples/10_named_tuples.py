# Named Tuples

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("Named tuple:", p)
print("x:", p.x, "y:", p.y)