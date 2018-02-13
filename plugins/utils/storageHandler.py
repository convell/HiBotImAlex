import os

def checkDir(file_path):
    directory = os.path.dirname(file_path)
    if not os.exists(directory):
        os.makedirs(directory)

def save(serverName,whatToSave):
    checkDir(join(os.getcwd(),serverName))
    open(join(os.getcwd(),serverName),r+)
    currentJson = load(serverName)
    for name,value in whatToSave:
        currentJson[name] = value

    
def load(serverName):
    checkDir(join(os.getcwd(),serverName))
    loadFile = open(join(os.getcwd(),serverName),r+)
    return loadFile.read()
