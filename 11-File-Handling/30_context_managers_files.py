# Context Managers Files

from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_manager(input("Enter filename: "), 'w') as f:
    f.write("Hello")