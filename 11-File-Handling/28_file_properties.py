# File Properties

import os

filename = input("Enter filename: ")
if os.path.exists(filename):
    stat = os.stat(filename)
    print(f"Size: {stat.st_size}")
    print(f"Modified: {stat.st_mtime}")
else:
    print("File not found")