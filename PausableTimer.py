import threading, time

class PausableTimer:
    def __init__(self, starttime, BPM, callback):
        self.starttime = starttime
        self.BPM = BPM
        self.callback = callback
        self.timeout = 60/BPM - ((time.time() - starttime) % (60/BPM))
        self.timer = threading.Timer(self.timeout, self.repeat())
        self.initTimer()

    def initTimer(self):
        self.timeout = 60/self.BPM - ((time.time() - self.starttime) % (60/self.BPM))
        
        self.timer.cancel()
        self.newTimer()
        self.startTime = time.time()

    def newTimer(self):
        self.timer = threading.Timer(self.timeout, self.repeat())

    def start(self):
        self.timer.start()

    def pause(self):
        self.timer.cancel()
        self.pauseTime = time.time()

    def resume(self):
        self.timer = threading.Timer(
            self.timeout - (self.pauseTime - self.startTime),
            self.callback)

        self.timer.start()

    def repeat(self):
        self.initTimer()
        self.callback