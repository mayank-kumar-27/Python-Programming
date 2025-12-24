# File Tell Seek

filename = input("Enter filename: ")
with open(filename, 'r') as f:
    print(f"Position: {f.tell()}")
    f.seek(5)
    print(f"After seek: {f.tell()}")
    content = f.read(5)
    print(content)