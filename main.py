from python_imagesearch.imagesearch import imagesearcharea
import time

bpm = 118
wCoordx1, wCoordy1, wCoordx2, wCoordy2 = 700, 800, 1200, 1080
starttime = time.time()
while True:
    pos1 =  imagesearcharea("images/unlevelledW.PNG", 700, 800, 1200, 1080)
    pos2 =  imagesearcharea("images/readyW.PNG", 700, 800, 1200, 1080)
    pos3 =  imagesearcharea("images/blueW.PNG", 700, 800, 1200, 1080)
    pos4 =  imagesearcharea("images/redW.PNG", 700, 800, 1200, 1080)
    pos5 =  imagesearcharea("images/goldW.PNG", 700, 800, 1200, 1080)
    pos6 =  imagesearcharea("images/cooldownW.PNG", 700, 800, 1200, 1080)
    if pos1[0] != -1:
        print("unlevelled W")
    elif pos2[0] != -1:
        print("ready W")
    elif pos3[0] != -1:
        print("blue")
    elif pos4[0] != -1:
        print("red")
    elif pos5[0] != -1:
        print("gold")
    elif pos6[0] != -1:
        print("cooldown W")
    else:
        print("image not found")
    time.sleep(60/bpm - ((time.time() - starttime) % (60/bpm)))