#
# Lab2.py (for the three problems assigned in Lab 2)
# Class: Programming I Lab
# Name: Jake Hennessy
# Date: 1/13/14
#
# Purpose: This program is intended to calculate values based on user input.

import math

def kilometersToMiles():
    
    # Compute the number of miles that John will travel, given the kilometers.
    # Input the kilometers, compute the miles (1 mile = 1.61 kilometers),
    #   and display the number of miles.

    # Introductions, and defintion of conversion factor.
    print("Welcome!")
    print("This program is intended to convert kilometers to miles.")
    MI_TO_KI = 1.61
    # Determining how many kilometers will be traveled.
    kilometers = eval(input("How many kilometers will be traveled?: "))
    # Calculate the number of miles.
    miles = kilometers / MI_TO_KI
    # Display the miles.
    print(miles, "miles will be traveled during this voyage.")


def shootingPercentage():
    
    # Compute the shooting percentage, given the number of shots taken
    #   and the number of shots made.

    # Introduction.
    print("Welcome!")
    # Determine how many shots were taken.
    shotsTaken = eval(input("How many shots has the player taken?: "))
    # Determine how many shots were made.
    shotsMade = eval(input("How many of those shots did the player make?: "))
    # Calculate the shooting percentage.
    shootingPercent = shotsMade / shotsTaken
    finalShotPercent = shootingPercent * 100
    # Display the percentage
    print("The players' shooting percentage is", finalShotPercent, "percent.")


def coffee():
    
    # Compute the cost of coffee orders. Each order costs $10.50 per pound.
    # Each order ships for $0.86 per pound, and there is a fixed cost of
    #   $1.50 per order for overhead.
    # Ask the user for the number of pounds in the order. Then calculate
    #   and display the cost.

    # Introduction.
    print("Welcome!")
    print("This program was made to determine the cost of a coffee order plus shipping.")
    # Input how many pounds in this order.
    poundsCoffee = eval(input("How many lbs. of coffee in this order?: "))
    # Calculate cost of the order, and define variables.
    costPerPound = 10.50
    shippingCost = 0.86
    costCoffee = poundsCoffee * costPerPound
    costShipping = poundsCoffee * shippingCost
    overheadCost = 1.50
    totalCost = costCoffee + costShipping + overheadCost    
    # Display the cost of the order
    print("The total cost of this order will be $", totalCost)


def triangleArea():
    
    # Calculate the area of a triangle given the length of its three sides,
    #   a, b, and c, using the formulas in the document.

    # Introductions.
    print("Welcome!")
    print("This program was created to calculate the area of any triangle, given the sides.")
    # Input the lengths of the sides, and determine units.
    unitsTriangle = input("What are the units being used?: ")
    sideA = eval(input("Please give the length of the first side: "))
    sideB = eval(input("Next, Please give the length of the second side: "))
    sideC = eval(input("Finally, please give the length of the last side: "))
    # Calculate s.
    s = (sideA + sideB + sideC) / 2
    # Calculate area (A), from s.
    A = math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))
    # Display the area
    print("The area of the triangle is", A, unitsTriangle, "squared.")
    

def sphere():
    
    # Calculate the volume and surface area of a sphere given its radius,
    #   using the formulas in the document.

    # Introduction.
    print("Welcome!")
    print("This program was created to calculate the volume and surface area of a sphere.")
    # Input the radius.
    unitsSphere = input("First, what are the units being used?: ")
    radiusSphere = eval(input("Please give me the radius of the sphere: "))
    # Calculate the volume and surface area.
    volumeSphere = ((4/3) * math.pi) * (radiusSphere ** 3)
    surfaceAreaSphere = 4 * math.pi * (radiusSphere ** 2)
    # Display the volume and surface area.
    print("The volume of the sphere will be", volumeSphere, unitsSphere, "cubed.")
    print("The surface area of the sphere will be", surfaceAreaSphere, unitsSphere, "squared.")

def main():
    kilometersToMiles()
    shootingPercentage()
    coffee()
    triangleArea()
    sphere()

main()




    
    

    

    

