# Path Operations

import os

path = input("Enter path: ")
print(f"Basename: {os.path.basename(path)}")
print(f"Dirname: {os.path.dirname(path)}")
print(f"Exists: {os.path.exists(path)}")
print(f"Is file: {os.path.isfile(path)}")
print(f"Is dir: {os.path.isdir(path)}")