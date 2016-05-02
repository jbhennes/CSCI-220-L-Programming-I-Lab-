# Circle.py

from Point import Point
from math import pi

class Circle:

    def __init__(self, x, y, r):
        self.r = 0.0
        self.center = Point()
        self.setCenter(x, y)

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.r

    def setCenter(self, x, y):
        self.center.setX(x)
        self.center.setY(y)
        
    def setRadius(self, r):
        if type(r) == float:
            self.r = r
        elif type(r) == int:
            self.r = float(r)

    def area(self):
        area = (2 * (pi) * self.r)
        return area

    def __str__(self):
        rtnStr = '\n\tCircle:\n'
        rtnStr += '\t  Center: ' + '(' + str(self.center.getX()) + ',' + str(self.center.getY()) + ')\n'
        rtnStr += '\t  Radius: ' + str(self.r) + '\n'
        rtnStr += '\t  Area: ' + str(self.area())
        return rtnStr
        
