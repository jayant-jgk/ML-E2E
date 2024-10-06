import os
from distutils.core import setup
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name ="Wine_Prediction"
list_of_files = \
    [ f"src/{project_name}/__init.py__",
  f"src/{project_name}/components/__init.py__",
  f"src/{project_name}/utilis/__init.py__",
  f"src/{project_name}/utilis/common.py",
  f"src/{project_name}/config/__init.py__",
  f"src/{project_name}/config/configuration.py",
  f"src/{project_name}/pipeline/__init.py__",
  f"src/{project_name}/entity/__init.py__",
  f"src/{project_name}/entity/config_entity.py",
  f"src/{project_name}/constants/__init.py__",
  "config/config.yaml",
  "params.yaml",
  "schema.yaml",
  "main.py",
  "app.py",
  "requirements.txt",
  "setup.py",
  "research/trials.ipynb",
  "templates/index.html"]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")














