# File Delete

import os

filename = input("Enter filename to delete: ")
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted")
else:
    print("File not found")