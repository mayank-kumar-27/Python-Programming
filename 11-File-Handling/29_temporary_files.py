# Temporary Files

import tempfile

with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write("Temporary content")
    print(f"Temporary file: {f.name}")