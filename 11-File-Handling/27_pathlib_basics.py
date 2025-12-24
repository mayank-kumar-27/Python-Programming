# Pathlib Basics

from pathlib import Path

path = Path(input("Enter path: "))
print(f"Name: {path.name}")
print(f"Suffix: {path.suffix}")
print(f"Parent: {path.parent}")
print(f"Exists: {path.exists()}")