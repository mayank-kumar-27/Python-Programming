# Dict Ordered Dict

from collections import OrderedDict
od = OrderedDict()
keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()
for k, v in zip(keys, values):
    od[k] = v
print("OrderedDict:", od)