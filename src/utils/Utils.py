from config.config import getServerConfig
import logging
from glob import glob

class Utils:
    
    @staticmethod
    def getFilesList():
        serverConfig = getServerConfig()
        datasetPath = serverConfig['datasetFileDir'] + '*.txt'
        filesList = glob(datasetPath)
        logging.info('List of dataset => %s', filesList)
        return filesList

    @staticmethod
    def initLoggingConfig(filepath):
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(filename=filepath, format=format,level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
