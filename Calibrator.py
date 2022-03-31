from python_imagesearch.imagesearch import imagesearcharea, imagesearch_region_loop

class Calibrator:
    def __init__(self, wCoordx1, wCoordy1, wCoordx2, wCoordy2):
        self.wCoordx1, self.wCoordy1, self.wCoordx2, self.wCoordy2 = wCoordx1, wCoordy1, wCoordx2, wCoordy2

    def calibrate(self):
        found = False
        while not found:
            blue =  imagesearcharea("images/blueW.PNG", self.wCoordx1, self.wCoordy1, self.wCoordx2, self.wCoordy2, precision = 0.95)
            red =  imagesearcharea("images/redW.PNG", self.wCoordx1, self.wCoordy1, self.wCoordx2, self.wCoordy2, precision = 0.95)
            gold =  imagesearcharea("images/goldW.PNG", self.wCoordx1, self.wCoordy1, self.wCoordx2, self.wCoordy2, precision = 0.95)

            if blue[0] != -1:
                startColor = "Blue"
                found = True 
            elif red[0] != -1:
                startColor = "Red"
                found = True
            elif gold[0] != -1:
                startColor = "Gold"
                found = True 
        
        if startColor == "Blue":
            imagesearch_region_loop("images/redW.PNG", 0.01, self.wCoordx1, self.wCoordy1, self.wCoordx2, self.wCoordy2, precision = 0.95)
            return "Red"
        elif startColor == "Red":
            imagesearch_region_loop("images/goldW.PNG", 0.01, self.wCoordx1, self.wCoordy1, self.wCoordx2, self.wCoordy2, precision = 0.95)
            return "Gold"
        elif startColor == "Gold":
            imagesearch_region_loop("images/blueW.PNG", 0.01, self.wCoordx1, self.wCoordy1, self.wCoordx2, self.wCoordy2, precision = 0.95)
            return "Blue"
        else:
            print("ERROR")
            print(startColor)