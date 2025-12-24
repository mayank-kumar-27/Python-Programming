# Dict Comprehension

keys = input("Enter keys separated by space: ").split()
values = [int(x) for x in input("Enter values separated by space: ").split()]
my_dict = {k: v for k, v in zip(keys, values)}
print("Dict:", my_dict)