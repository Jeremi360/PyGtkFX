import os

def getfile(*path):
    return os.path.abspath(os.path.join(*path))
