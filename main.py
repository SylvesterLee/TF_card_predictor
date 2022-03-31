from python_imagesearch.imagesearch import imagesearcharea
import time
from Calibrator import Calibrator
from PausableTimer import PausableTimer
from StateMachine import StateMachine

BPM = 116
starttime = time.time()

calibrator = Calibrator(750, 900, 950, 1100)
startColor = calibrator.calibrate()
#startColor = "Red"

stateMachine = StateMachine(startColor)

stateMachine.rotateColor()
stateMachine.rotateColor()
time.sleep(0.24)

timer = PausableTimer(60/BPM, stateMachine.rotateColor)


while True:    
    timer.newTimer()
    #update UI color stateMachine.getColor()
    print(stateMachine.getColor())
    time.sleep(60/BPM - ((time.time() - starttime) % (60/BPM)))
    #time.sleep(0.5)






'''
bpm = 200
wCoordx1, wCoordy1, wCoordx2, wCoordy2 = 750, 900, 950, 1100
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
    time.sleep(60/bpm - ((time.time() - starttime) % (60/bpm)))'''