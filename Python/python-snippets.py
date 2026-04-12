# The best way to get the path of a file in Python is to use the pathlib library, 
# which provides an easy and efficient way to handle file paths.
# Path.resolve.parents is used to go up in the directory structure, 
# and you can specify how many levels to go up 
# by replacing "NUMBER OF FOLDERS TO GO UP" with the appropriate number.
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents["NUMBER OF FOLDERS TO GO UP"]
labels_path = BASE_DIR / "other_folder" / "file.txt"  # path to the labels file