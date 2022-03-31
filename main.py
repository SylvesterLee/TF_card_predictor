from python_imagesearch.imagesearch import imagesearcharea
import time

bpm = 200
wCoordx1, wCoordy1, wCoordx2, wCoordy2 = 750, 900, 950, 1050
starttime = time.time()
while True:
    pos1 =  imagesearcharea("images/unlevelledW.PNG", wCoordx1, wCoordy1, wCoordx2, wCoordy2, precision = 0.95)
    pos2 =  imagesearcharea("images/readyW.PNG", wCoordx1, wCoordy1, wCoordx2, wCoordy2, precision = 0.95)
    pos3 =  imagesearcharea("images/blueW.PNG", wCoordx1, wCoordy1, wCoordx2, wCoordy2, precision = 0.95)
    pos4 =  imagesearcharea("images/redW.PNG", wCoordx1, wCoordy1, wCoordx2, wCoordy2, precision = 0.95)
    pos5 =  imagesearcharea("images/goldW.PNG", wCoordx1, wCoordy1, wCoordx2, wCoordy2, precision = 0.95)
    pos6 =  imagesearcharea("images/cooldownW.PNG", wCoordx1, wCoordy1, wCoordx2, wCoordy2, precision = 0.95)
    if pos1[0] != -1:
        print("unlevelled W")
    elif pos2[0] != -1:
        print("ready W")
        print(pos2[0], pos2[1])
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