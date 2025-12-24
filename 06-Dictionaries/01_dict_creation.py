# Dict Creation

keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()
my_dict = dict(zip(keys, values))
print("Dict:", my_dict)