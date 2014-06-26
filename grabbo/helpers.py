import os

def getfile(*path):
    os.path.abspath(os.path.join(*path))
