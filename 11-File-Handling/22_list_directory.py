# List Directory

import os

dir_name = input("Enter directory name: ")
files = os.listdir(dir_name)
print(files)