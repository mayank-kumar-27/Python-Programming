# Matrix 2D Lists

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    row = [int(x) for x in input(f"Enter row {i+1} separated by space: ").split()]
    matrix.append(row)
print("Matrix:")
for row in matrix:
    print(row)