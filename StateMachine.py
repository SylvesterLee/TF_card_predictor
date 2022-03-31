from concurrent.futures.process import _ExceptionWithTraceback


class StateMachine:
    def __init__(self, startColor):
        self.currentColor = startColor

    def setColor(self, color):
        self.currentColor = color
    
    def rotateColor(self):
        if self.currentColor == "Blue":
            self.currentColor = "Red"
        elif self.currentColor == "Red":
            self.currentColor = "Gold"
        elif self.currentColor == "Gold":
            self.currentColor = "Blue"
        else:
            raise BaseException
    
    def getColor(self):
        return self.currentColor