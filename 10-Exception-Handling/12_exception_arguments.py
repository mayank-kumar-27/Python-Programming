# Exception Arguments

try:
    raise ValueError("Invalid value", "extra info")
except ValueError as e:
    print(f"Error: {e}")
    print(f"Args: {e.args}")