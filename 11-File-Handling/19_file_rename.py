# File Rename

import os

old_name = input("Enter current filename: ")
new_name = input("Enter new filename: ")
os.rename(old_name, new_name)
print("File renamed")