## lab4.py
##
## Name: Jake Hennessy
## I certify that this lab is my own work.
##
## Lab 3 - Graphics
## Objectives:
##  1.) Discussion #3, Graphics chapter of Zelle text
##  2.) Moves a circle based on user clicks
##  3.) Comments added: RHS

from graphics import *
from math import *
import time

#1 Modify as directed
def squares():

    #Creates a graphical window
    win = GraphWin("Lab 4 - Click Squares", 400, 400)
    width = win.getWidth()
    height = win.getHeight()

    #Number of times user can move circle
    numClicks = 5

    # Create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move circle")
    instructions.draw(win)

    # Builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # Allows the user to click multiple times to move the
    #   circle
    # Creating new circles
    for i in range(numClicks):
        p1 = win.getMouse()
        c = shape.getCenter()
        shape2 = shape.clone()
        #move amount is distance from center of circle to the
        #point where the user clicked
        dx = p1.getX() - c.getX()
        dy = p1.getY() - c.getY()
        shape.move(dx, dy)
        shape2.draw(win)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

squares()

def rectangle():
    """
    Add the function rectangle() to your code and do Chapter 4,
    Programming Exercise 9 (p. 119), instructions are provided in the
    comments for the function. Display the numerical output in the
    graphics window – don't use print. Ask the user to click to end
    the program, and be sure to close the window at the end. Make the
    window 400 by 400.
    """
    # This program displays information about a rectangle drawn by the user.
    # Create window
    win2 = GraphWin("This Rectangle Here", 400, 400)
    # Set Points.
    point = win2.getMouse()
    point.draw(win2)
    point2 = win2.getMouse()
    point2.draw(win2)
    # Draw Rectangle.
    rect = Rectangle(point, point2)
    rect.setFill("cyan")
    rect.setOutline("red2")
    rect.draw(win2)
    # Calculate the Area and the Perimeter in the window.
    length = abs((point2.getX())-(point.getX()))
    width = abs((point2.getY())-(point.getY()))
    area = (length)*(width)
    p = length + width
    perimeter = p*2
    # Output the area and perimeter.
    textA = Text(Point(200, 350),"The Area is: " + str(area) + " pixels squared.")
    textP = Text(Point(200, 375),"The Perimeter is: " + str(perimeter) + " pixels.")
    textA.setFace('times roman')
    textP.setFace('times roman')
    textA.setStyle('bold')
    textP.setStyle('bold')
    textA.setSize(20)
    textP.setSize(20)
    textA.draw(win2)
    textP.draw(win2)
    # Close the window!
    time.sleep(5)
    textA.undraw()
    textP.undraw()
    textClose = Text(Point(100, 375),"Click to Close!")
    textClose.setFace('helvetica')
    textClose.setStyle('bold italic')
    textClose.setSize(20)
    textClose.draw(win2)
    win2.getMouse()
    win2.close()

rectangle()

def circle():
    """
    Add a function called circle() to draw a circle. The first mouse
    click determines the center of the circle. The second mouse click
    determines a point on its circumference.
    Ask the user to click to end the program, and close the window at the end.
    """
    # Make a Window.
    win = GraphWin("THE CIRCLE GAME!!!", 500, 500)
    # Obtain information from a couple of mouse clicks, and plot them.
    center = win.getMouse()
    center.draw(win)
    circumference = win.getMouse()
    circumference.draw(win)
    # Calculate Euclidean distance.
    eDistance = sqrt(((abs(circumference.getX())-(center.getX()))**2)+((abs(circumference.getY())-(center.getY()))**2))
    # Draw circle user has created.
    circle = Circle(center, eDistance)
    circle.setFill("red2")
    circle.setOutline("blue1")
    circle.draw(win)
    # Display radius
    textR = Text(Point(200, 350),"The radius is: " + str(eDistance) + " pixels.")
    textR.setFace('times roman')
    textR.setStyle('bold')
    textR.setSize(20)
    textR.draw(win)
    # Close the window!
    time.sleep(5)
    textR.undraw()
    textClose = Text(Point(100, 375),"Click to Close!")
    textClose.setFace('helvetica')
    textClose.setStyle('bold italic')
    textClose.setSize(20)
    textClose.draw(win)
    win.getMouse()
    win.close()

circle()

def pi2():
    """
    Write a function, pi2(), to approximate the value of pi by summing the
    terms of this series:4/1 – 4/3 + 4/ 5 – 4/7 + 4/9 – 4/11 + ….
    The program should prompt the user for n, the number of terms to sum,
    and then output the sum of the first n terms of this series.
    Have your function subtract from the value of math.pi to see how
    accurate it is...
    """
    # Introduction.
    print("Welcome! \n This program will allow you to calculate pi based on n, \n the number of terms that will be used in the calculation.")
    # Get variable for n.
    n = eval(input("How many terms will be used in the calculation? \n n = "))
    # Calculate the fractions necessary.
    num = 4
    denominator = 1
    signReverse = 1
    total = 0
    for i in range(n):
        term = (num/denominator) * signReverse
        total = term + total
        denominator = denominator + 2
        signReverse = signReverse * -1
    # Print the approximation
    print("the approximation of pi in", n, "terms is", total)
    # Print the difference.
    diff = pi - total
    print("the discrepancy is", diff)

pi2()

