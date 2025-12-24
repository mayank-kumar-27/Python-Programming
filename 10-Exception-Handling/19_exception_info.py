# Exception Info

import sys

try:
    raise ValueError("Test error")
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"Type: {exc_type}")
    print(f"Value: {exc_value}")