import os
from common import app

def SetupEnv():
    _CheckCreateDir(app.config['LOG_FOLDER'])
    _CheckCreateDir(app.config['UPLOAD_FOLDER'])
    
def _CheckCreateDir(dir):
    if not os.path.exists(dir):
        print("Creating environment folderss")
        os.makedirs(dir)

import importlib
def ImportAllFromDir(dir, prefix=""):
    files = os.listdir(dir)
    for file in files:
        if file.endswith(".py") and file != __name__:
            cleanName = file[:-3]
            importlib.import_module(prefix + cleanName)
