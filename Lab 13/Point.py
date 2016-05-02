# Point.py

class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        if type(x) == int:
            self.x = x

    def setY(self, y):
        if type(y) == int:
            self.y = y

    def __str__(self):
        rtnStr = '\n\tPoint:\n'
        rtnStr += '\t  x: ' + str(self.x) + '\n'
        rtnStr += '\t  y: ' + str(self.y)
        return rtnStr
