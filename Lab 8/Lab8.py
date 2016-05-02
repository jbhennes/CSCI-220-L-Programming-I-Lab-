# CSCI 220L - Lab 8 Solutions
#
# Name 1: Asia Smith 
#
# Name 2: Jake Hennessy
#

import math

# Chapter 6, Exercise 3
def sphereArea(radius):
    """
    Function to compute the area (A = 4πr^2) of a sphere.
    """
    area = (4 * math.pi) * (radius**2)
    return area

def sphereVolume(radius):
    """
    Function to compute the volume (V = 4/3πr^3) of a sphere.
    """
    volume = (4/3 * math.pi) * (radius**3)
    return volume

def testSphereFunctions():
    testRadius = eval(input("Enter radius amount: "))
    testUnits = input("Enter unit value: ")
    area = round(sphereArea(testRadius), 2)
    volume = round(sphereVolume(testRadius), 2)
    print("Area: ", (area), (testUnits), "squared.")
    print("Volume: ", (volume), (testUnits), "cubed.")
          


    
#testSphereFunctions()

# Chapter 6, Exercise 4
def sumN(n):
    """
    Function to compute the sum of the first N natural numbers.
    """
    numList = []
    num = 0
    for num in range(n + 1):
        num += num
##    for num in range(n):
##        numList.append(num)
##    total = sum(numList)
##    return total
    return num

def sumNCubes(n):
    """
    Function to compute the sum of the cubes of the first N natural numbers.
    """
    numCubeList = []
    for num in range(n + 1):
        numCube = (num**3)
        numCubeList.append(numCube)
    cubeTotal = sum(numCubeList)
    return cubeTotal



def testSumFunctions():
    # Obtain input for user (N, number to start)
    numberOfTerms = eval(input("Please enter the amount of numbers to use (N): "))
    # startNum = eval(input("Please enter the number to begin calculations with: "))
    sumNum = sumN(numberOfTerms)
    sumNumCube = sumNCubes(numberOfTerms)
    # Output results.
    print("the sum of the terms is:\n\t", (sumNum))
    print("the sum of the cubes of the terms is:\n\t", (sumNumCube))
    


#testSumFunctions()

# chapter 6, exercise 11
def squareEach(nums):
    """
    Function to square each number in a list. Returns nothing.
    """
    for i in range(len(nums)):
        nums[i] = (nums[i] ** 2)

# chapter 6, exercise 12
def sumList(nums):
    """
    Function to add the numbers in a list. Returns the sum.
    """
    totals = sum(nums)
    return totals

# chapter 6, exercise 13
def toNumbers(strList):
    """
    Function to convert a list of numbers in string form to
    numerical form. Returns nothing.
    """
    for i in range(len(strList)):
        strList[i] = eval(strList[i])

# chapter 6, exercise 14
def solve():
    """
    Function to read numbers from a file and display the sum of
    the squares of the numbers. Uses the three previous functions.
    """
    inFileName = input('What is the name of the file (w/ .txt extension): \n')
    inFile = open((inFileName), 'r')

    for line in inFile:
        strNumList = line.split()
    toNumbers(strNumList)
    squareEach(strNumList)
    squareTotals = sumList(strNumList)
    print('The sum of the numbers squared in the file is: \n', squareTotals)

solve()

def sumOfSquares():
    """
    Code to test exercise 11 - square numbers in a list
    """
    



    
    """
    Code to test exercise 12 - sum numbers in a list
    """



    
    """
    Code to test exercise 13 - sum list of strings to numbers
    """



    
    """
    Code to test exercise 14 - display the sum of the squares of the
    numbers on a file, using the three previous functions.
    """



    
#sumOfSquares()

