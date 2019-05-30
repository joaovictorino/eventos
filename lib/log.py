import logging
from logging.handlers import TimedRotatingFileHandler
import common
import os

app = common.app
def SetupLog(logName):
    logFileName = os.path.join(app.config["LOG_FOLDER"], app.config["LOG_FILENAME"])
    
    logger = logging.getLogger(logName)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
    fh = logging.FileHandler(logFileName)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    lh = TimedRotatingFileHandler(logFileName, when="midnight", interval=1)
    logger.addHandler(lh)
    
    logger.setLevel(app.config["LOG_LEVEL"])
    
    return logger
