import json

def getServerConfig():
    with open('../config/server.json') as serverConfig:
        jsonServerConfig = json.load(serverConfig)
        return jsonServerConfig