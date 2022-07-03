from flask import Flask
from config.config import getServerConfig
import logging
import os
from utils.Utils import Utils
from restapis.searchData import searchData

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'some secret key'

app.add_url_rule("/", view_func=searchData.as_view("search_Data"))

serverConfig = getServerConfig()
logFileDir = serverConfig['logFileDir']

if os.path.exists(logFileDir) == False:
    print("LogFile Directory " + logFileDir +
          " does not exist. Exiting the app.")
    exit(-1)

print("LogFile Directory = " + logFileDir)
Utils.initLoggingConfig(logFileDir + "/app.log")

logging.info('serverConfig => %s', serverConfig)

port = serverConfig['port']

if __name__ == "__main__":
    app.run('localhost',port)
