import time
import azureEssentials as aze
print('init')
hasPlayed = False
dataf = open(aze.localize("data.txt"),"r")
data = str(dataf.read())
data = data.split(",")
datad = dict()
work = str()
for e in data:
    work = e
    datad[str(work[0:-1])] = str(work[-1])
print(datad)
while True:
    corrt = time.ctime(time.time())
    dateList = str(corrt).split()
    hmin = dateList[3].split(":")
    if hmin[2] == "00":
        hasPlayed = False
    chm = str(hmin[0] + hmin[1])
    print(chm)
    if aze.isWeekDay(dateList[0]):
        print("Hétköznap van")
        if not(datad.get(chm) == "None"):
            if hasPlayed == False:
                if datad.get(chm) == "r":
                    aze.playSound(1)
                elif datad.get(chm) == "h":
                    aze.playSound(2)
            hasPlayed = True
    else:
        print("Nem hétköznap van")
    time.sleep(1)