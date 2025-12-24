# Nested Lists

rows = int(input("Enter number of rows: "))
nested_list = []
for i in range(rows):
    row = input(f"Enter row {i+1} separated by space: ").split()
    nested_list.append(row)
print("Nested list:", nested_list)