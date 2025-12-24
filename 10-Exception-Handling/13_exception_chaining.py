# Exception Chaining

try:
    try:
        raise ValueError("Original error")
    except ValueError:
        raise RuntimeError("Chained error") from ValueError("Original error")
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Cause: {e.__cause__}")