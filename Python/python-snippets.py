# The best way to get the path of a file in Python is to use the pathlib library, 
# which provides an easy and efficient way to handle file paths.
# Path.resolve.parents is used to go up in the directory structure, 
# and you can specify how many levels to go up 
# by replacing "NUMBER OF FOLDERS TO GO UP" with the appropriate number.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents["NUMBER OF FOLDERS TO GO UP"]
labels_path = BASE_DIR / "other_folder" / "file.txt"  # path to the labels file


# __________________ SEPARATION BETWEEN CODE SNIPPETS __________________


# This is how to call a python module from another folder, 
# that is following this structure:
# project/
# ├── src/
# |   ├── python/
# │     ├── main.py
# ├── tests/
# │   ├── module.py
# In this case, you can import the main.py in module.py like this:

import sys, os
# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import using the full module path from the root
from src.python import main


# __________________ SEPARATION BETWEEN CODE SNIPPETS __________________


