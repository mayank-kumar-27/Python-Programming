# Create Directory

import os

dir_name = input("Enter directory name: ")
os.makedirs(dir_name, exist_ok=True)
print("Directory created")