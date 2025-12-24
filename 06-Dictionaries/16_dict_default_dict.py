# Dict Default Dict

from collections import defaultdict
dd = defaultdict(int)
keys = input("Enter keys separated by space: ").split()
for key in keys:
    dd[key] += 1
print("Defaultdict:", dict(dd))