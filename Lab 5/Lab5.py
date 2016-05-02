# Lab5.py
# Name 1: Aaron Walton
# Name 2: Jake Hennessy

from graphics import *
from math import *
import time

def cupConverter():
    
    # Author: RoxAnn H. Stalvey, modified by Walter Pharr
    # Illustrates getting numeric input through graphics window

    win = GraphWin("Convert cups to milliliters", 300, 200)

    # Specify the message for the input box
    boxDesc = Text(Point(100, 50), "Input cups: ")
    boxDesc.draw(win)

    # Create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setText("0")
    inp.draw(win)
    

    # Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    # This button isn't necessary, but it makes a nice point for the user
    #  to click.  If you click anywhere in the window, the code reacts
    #  the same way.
    button = Text(Point(150, 100), "Click")
    button.draw(win)
    border = Rectangle(Point(115, 80), Point(185, 120))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    cups = eval(inp.getText())

    # Calculate milliliter equivalent here
    cupsToMl = cups*236.588

    # Display output and change button
    output.setText("Number of Millimeters = " + str(round(cupsToMl,3)))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()

cupConverter()

def target():
    #Create Window
    win = GraphWin("Archery Target", 500, 500)

    # Add code here to get the dimensions and draw the target
    width = win.getWidth()
    height = win.getHeight()

    # Draw circle
    point = Point((width/2), (height/2))
    c = Circle(point, (width/2))
    c.setFill("white")
    c1 = Circle(point, ((width/2) * .8))
    c1.setFill("black")
    c2 = Circle(point, ((width/2) * .6))
    c2.setFill("blue")
    c3 = Circle(point, ((width/2) * .4))
    c3.setFill("red")
    c4 = Circle(point, ((width/2) * .2))
    c4.setFill("yellow")

    #draw circles
    c.draw(win)
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    c4.draw(win)

    #create text that tells user to close
    textPoint = Point((width/2), height * .95)
    closeText = Text(textPoint, "Click to Close")
    closeText.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()

target()

def triangle():
    win = GraphWin("Draw a Triangle", 500, 500)

    # Add code here to accept the mouse clicks, draw the triangle.
    #   and display its area in the graphics window.

    # Defining the number of clicks
    numclicks = 3

    # Creating empty lists to hold coordinate values
    xcord = []
    ycord = []

    # Defining points for textanchors
    textpoint = Point((win.getWidth()/2),win.getHeight()*.90)
    textpoint2 = Point((win.getWidth()/2),win.getHeight()*.95)

    # Loop to input the user's clicks
    for i in range(numclicks):
        p=win.getMouse()
        xcord.append(p.getX())
        ycord.append(p.getY())
        p.draw(win)

    # Creation of the shape
    shape=Polygon(Point(xcord[0],ycord[0]), Point(xcord[1],ycord[1]), Point(xcord[2],ycord[2]))
    shape.draw(win)
    shape.setFill("peachpuff")
    
    # Define delta x and delta y.
    side1X = abs(xcord[0] - xcord[1])
    side2X = abs(xcord[1] - xcord[2])
    side3X = abs(xcord[2] - xcord[0])
    side1Y = abs(ycord[0] - ycord[1])
    side2Y = abs(ycord[1] - ycord[2])
    side3Y = abs(ycord[2] - ycord[0])
    
    # Enter the euclidean dist. formula
    length1 = sqrt((side1X**2) + (side1Y**2))
    length2 = sqrt((side2X**2) + (side2Y**2))
    length3 = sqrt((side3X**2) + (side3Y**2))
    
    # calculate perimeter.
    perimeter = round(length1 + length2 + length3, 2)
    
    # calculate the area.
    s = (length1 + length2 + length3) / 2
    area = round(sqrt(s * (s - length1) * (s - length2) * (s - length3)), 2)

    # Relay data to the shell
    print(ycord)
    print(xcord)
    print(perimeter, area)

    # Creating and darwing text
    AreaText = Text(textpoint, "Area: "+str(area)+ " units squared.")
    PerimText = Text(textpoint2, "Perimeter: " + str(perimeter)+ " units.")
    AreaText.draw(win)
    PerimText.draw(win)
    
    # click to close command
    time.sleep(3)
    AreaText.undraw()
    PerimText.undraw()
    closeCommand = Text(textpoint, "Click to Close")
    closeCommand.draw(win)
    
    # Wait for another click to exit
    win.getMouse()
    win.close()
   
triangle()






