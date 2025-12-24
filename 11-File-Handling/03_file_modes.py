# File Modes

# 'r' - read, 'w' - write, 'a' - append, 'b' - binary, '+' - read/write
mode = input("Enter mode (r/w/a): ")
filename = input("Enter filename: ")
with open(filename, mode) as f:
    if 'r' in mode:
        print(f.read())
    else:
        f.write("Sample text")