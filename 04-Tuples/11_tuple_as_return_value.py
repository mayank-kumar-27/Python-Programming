# Tuple As Return Value

def get_coords():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    return (x, y)

coords = get_coords()
print("Coordinates:", coords)