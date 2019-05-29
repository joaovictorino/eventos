import logging
from logging.handlers import TimedRotatingFileHandler
import common

app = common.app
def SetupLog(logName):
    logger = logging.getLogger(logName)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
    fh = logging.FileHandler(app.config["LOG_FILENAME"])
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    lh = TimedRotatingFileHandler(app.config["LOG_FILENAME"], when="midnight", interval=1)
    logger.addHandler(lh)
    
    logger.setLevel(app.config["LOG_LEVEL"])
    
    return logger
