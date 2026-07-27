# Markdown / HTML Snippets to create the header of the notebook for UdeA projects.

# <p>
#   <img src="https://upload.wikimedia.org/wikipedia/commons/f/fb/Escudo-UdeA.svg"
#        alt="UdeA logo"
#        height="190px"
#        align="left"
#        hspace="15px">
# </p>

# <h1 style="margin-top: 20px;"><b>Name of the project</b></h1>

# <hr>

# <div align="right" style="font-size: 14px; line-height: 1.4;">
#   <b>Estiven Castrillon Alzate</b><br>
#   Institute of Physics<br>
#   <i>Universidad de Antioquia</i><br>
#   <span style="font-size: 12px;">Date: ...</span>
# </div>

# <br><br>

# 


# __________________ SEPARATION BETWEEN CODE SNIPPETS __________________


# This is how to call a python module from another folder inside a jupyter notebook, 
# that is following this structure:
# project/
# ├── src/
# |   ├── python/
# │     ├── main.py
# ├── tests/
# │   ├── module.py
# In this case, you can import the main.py in module.py like this:
import sys
import os

# General path for the project
project_root = os.path.abspath(os.path.join(os.getcwd(), "../.."))
print("Project root:", project_root)

sys.path.append(project_root)

from src.python import main

# __________________ SEPARATION BETWEEN CODE SNIPPETS __________________