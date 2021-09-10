import time
import os

dir = str(os.path.dirname(os.path.abspath(__file__)))

def pir(onoff):
    if onoff == 1:
        os.system(str(dir) + r"\Ring\ringOn.bat")
    else:
        os.system(str(dir) + r"\Ring\ringOff.bat")

def ring(length):
    pir(1)
    time.sleep(length)
    pir(0)
