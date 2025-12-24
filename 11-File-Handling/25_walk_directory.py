# Walk Directory

import os

dir_name = input("Enter directory name: ")
for root, dirs, files in os.walk(dir_name):
    print(f"Root: {root}")
    print(f"Dirs: {dirs}")
    print(f"Files: {files}")