import os
dir = str(os.path.dirname(os.path.abspath(__file__)))
def localize(file):
    return(dir + "\\" + str(file))
def playSound(index):
    os.system(str(dir) + "\sound.bat " + str(index))
def isWeekDay(day):
    if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thu" or day == "Fri":
        return(True)
    else:
        return(False)