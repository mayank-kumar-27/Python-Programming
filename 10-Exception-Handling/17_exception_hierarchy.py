# Exception Hierarchy

# BaseException
#  |- Exception
#     |- ValueError, TypeError, etc.

try:
    raise ValueError("Value error")
except Exception as e:
    print(f"Caught Exception: {e}")
except BaseException as e:
    print(f"Caught BaseException: {e}")