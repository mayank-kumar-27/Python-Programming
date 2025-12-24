# Dict Fromkeys

keys = input("Enter keys separated by space: ").split()
value = input("Enter default value: ")
my_dict = dict.fromkeys(keys, value)
print("Dict:", my_dict)