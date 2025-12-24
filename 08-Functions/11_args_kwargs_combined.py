# Args Kwargs Combined

def func(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

args_input = input("Enter args separated by space: ").split()
kwargs_input = input("Enter kwargs as key=value pairs separated by space: ").split()
kwargs = {}
for item in kwargs_input:
    key, value = item.split('=')
    kwargs[key] = value
func(*args_input, **kwargs)