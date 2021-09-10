import time
import os

dir = str(os.path.dirname(os.path.abspath(__file__)))

def ring(length):
    if length == 0.5:
        os.system(str(dir) + r"\Ring\dotfive.bat")
    elif length == 1:
        os.system(str(dir) + r"\Ring\one.bat")
    elif length == 2:
        os.system(str(dir) + r"\Ring\two.bat")
    elif length == 3:
        os.system(str(dir) + r"\Ring\three.bat")
    else:
        os.system(str(dir) + r"\Ring\five.bat")
