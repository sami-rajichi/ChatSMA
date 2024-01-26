import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "Src/__init__.py",
    "Src/helper.py",
    "Src/prompt.py",
    ".env",
    "app_info.py",
    "chatsma.py",
    "pinecone_index_store.py",
    "Static/.gitkeep",
    "HTMLTemplates/chatbot.html"
]


for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir != "":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory -> {filedir}.")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         logging.info(f"Creating empty file -> {filepath}.")
         pass

   else:
      logging.info(f"{filename} is already existed.")