#!/usr/bin/env python
from acropalypse import Acropalypse
import sys, os
import tempfile

if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} </path/to/img>") # E: invalid syntax
    exit(1)

TEMPDIR = tempfile.gettempdir()
ACROPALYPSE = Acropalypse()
ACROPALYPSE.reconstruct_image(sys.argv[1], 1920, 1080, True)
print ("Reconstructed image saved to: " + os.path.join(TEMPDIR, 'restored.png'))
