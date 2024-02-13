import os, sys
from pathlib import Path
import logging 

while True:
    project_name = input("Enter your project name")
    if project_name !="":
        break

#src/__init__.pyexit
#src/components/__init__.py
# creating a different different file inside a src file
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]

#spitting all file to make sure as individual
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # This line splits the file path into its directory part

    if filedir !="":                            # This line checks if the directory part of the file path is not empty.
        os.makedirs(filedir,exist_ok=True)       #  If it's not empty, it creates the directory using 

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  # This line checks if the file does not exist or if its size is zero.
        with open(filepath,"w") as f:           # If the file doesn't exist or its size is zero, it opens the file in write mode ("w") 
            pass                                # and immediately closes it without writing anything. This effectively creates an empty file.
    else:
        logging.info("file is already present at : {filepath}")   # If the file already exists and is not empty, it logs an informational message indicating that the file is already present at the given path.

"""In summary, this code iterates over a list of file paths, ensures that the directories for each file exist, 
and creates empty files for those that don't exist or are empty. If a file already exists and is not empty,
 it logs a message indicating its presence.

"""