# File Copy

import shutil

src = input("Enter source filename: ")
dst = input("Enter destination filename: ")
shutil.copy(src, dst)
print("File copied")