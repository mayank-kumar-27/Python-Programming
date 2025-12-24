# Dict Chain Map

from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain = ChainMap(dict1, dict2)
print("ChainMap:", dict(chain))