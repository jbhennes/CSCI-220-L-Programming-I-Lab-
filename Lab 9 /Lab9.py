## Lab9.py
##
## Name 1: Jake Hennessy
##
## Name 2: Matt Glaser
##

from graphics import *
from math import sqrt

def starter():
    """
    Ask for a wrestler's weight and number of wins, determine whether
    the wrestler is a starter.
    """
    weight = round(eval(input('What is the weight of the wrestler?: ')), 2)
    numWins = eval(input('What are the number of wins for the wrestler?: '))
    if 150 <= weight < 160 and numWins >= 5:
        print('This wrestler will start!')
    elif weight > 199 and numWins > 20:
        print('This wrestler will start!')
    else:
        print('This wrestler will warm the bench this season!')

#starter()



def isbn():
    """
    Ask for a book's ISBN, determmine whether it is a valid number.
    """
    counter = 10
    sumISBN = 0
    ISBN = input('What is the ISBN of the book in question?: ')
    for num in ISBN :
        sumISBN = sumISBN + (int(num) * counter)
        counter += -1
    print('The sum of the ISBN is: ', sumISBN)


#isbn()



def circleOverlap():
    """
    Draw two circles and determine whether they overlap.
    """
    #Build window
    winHeight = 400
    winWidth = 400
    win = GraphWin("Overlapping circles", winHeight, winWidth)
    win.setBackground('black')

    #Text area for instructions for user
    instruct = Text(Point(winWidth/2, winHeight-10), "")
    instruct.setTextColor('white')
    instruct.setStyle('bold italic')
    instruct.draw(win)

    ## Making the circles!
    #Get center point and x/y for center of circle 1
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center1 = win.getMouse()
    center1.draw(win)
    cX1 = center1.getX()
    cY1 = center1.getY()
    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle to draw")
    border1 = win.getMouse()
    bX1 = border1.getX()
    bY1 = border1.getY()
    #Calculate radius1 using Euclidean distance
    radius1 = sqrt((cX1-bX1) ** 2 + (cY1-bY1) ** 2)
    circle1 = Circle(center1, radius1)
    circle1.setFill('cyan')
    circle1.draw(win)
    #Get center point and x/y for center of circle 2
    instruct.setText("For circle #2, click the centerpoint for the circle")
    center2 = win.getMouse()
    center2.draw(win)
    cX2 = center2.getX()
    cY2 = center2.getY()
    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle to draw")
    border2 = win.getMouse()
    bX2 = border2.getX()
    bY2 = border2.getY()
    #Calculate radius2 using Euclidean distance
    radius2 = sqrt((cX2-bX2) ** 2 + (cY2-bY2) ** 2)
    circle2 = Circle(center2, radius2)
    circle2.setFill('tomato')
    circle2.draw(win)
    # Calculate the distance between the circles
    totalDistance = sqrt((cX2-cX1) ** 2 + (cY2-cY1) ** 2)
    #Perform the calculation to determine whethere there is circle overlap
    if ((radius1) + (radius2)) >= totalDistance :
        result = Text(Point(winWidth/2, winHeight/2), "Circles Overlap!")
        result.setTextColor('lime green')
        result.setSize(24)
        result.setStyle('bold italic')
        result.setFace('helvetica')
        result.draw(win)
    else:
        result = Text(Point(winWidth/2, winHeight/2), "Circles Do Not Overlap!")
        result.setTextColor('lime green')
        result.setSize(24)
        result.setFace('helvetica')
        result.setStyle('bold italic')
        result.draw(win)
    # Printing radii
    print("radius of circle 1 :", radius1, "\nradius of circle 2 :", radius2)
    # Wait for another click to exit
    instruct.undraw()
    instruct.setText("Click anywhere to close.")
    instruct.draw(win)
    win.getMouse()
    win.close()

circleOverlap()


def leapYear():
    """
    A year is a leap year if it is evenly divisible by 4.
    However, that adds too many days, so a year is not a leap year
    if it is evenly divisible by 100. But then the year is a bit too short,
    so a year that is evenly divisible by 400 is a leap year.
    (So February 29, 2000, was a very special day.
    There won't be another leap day in a century year until 2400.)
    """
    year = eval(input('What is the year?: '))
    if ((year % 400) == 0) or ((year % 4) == 0) and not ((year % 100) == 0):
        print( year, 'is a leap year!')
    else:
        print( year, 'is not a leap year!')
    
#leapYear()

