import os
from common import app

def SetupEnv():
    _CheckCreateDir(app.config['LOG_FOLDER'])
    _CheckCreateDir(app.config['UPLOAD_FOLDER'])
    
def _CheckCreateDir(dir):
    if not os.path.exists(dir):
        print("Creating environment folderss")
        os.makedirs(dir)
