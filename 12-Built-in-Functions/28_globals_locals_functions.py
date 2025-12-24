# Globals Locals Functions

global_var = "I'm global"

def func():
    local_var = "I'm local"
    print(f"Globals: {list(globals().keys())[:5]}...")
    print(f"Locals: {locals()}")

func()