# File Exists Check

import os

filename = input("Enter filename: ")
if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exist")