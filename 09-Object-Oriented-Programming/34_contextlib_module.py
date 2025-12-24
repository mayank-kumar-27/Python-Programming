# Contextlib Module

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering")
    yield
    print("Exiting")

with my_context():
    print("Inside")