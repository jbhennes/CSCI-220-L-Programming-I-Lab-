## lab3.py
##
## The purpose of this program is to calculate the sum of squares defined
##  by the user, the power of numbers as defined by user input, the Fibonacci
##  sequence, and finally to calculate pi.
##
## Name: Jake Hennesssy
##  I certify that this lab is my own work.
## Class: CSCI 220L - Programming Lab
## Prof: Stalvey
## Date: 1.27.2014


def sumSquares():
    """
    Write a function sumSquares() that calculates the sum of the squares
    of the numbers in a given range.   The function should allow the user
    to input the starting and ending numbers within the range.  For example
    if the user inputs 3 as the lower range and 5 as the upper range, the
    function should return the result of the equation 32+42+52 which is 50.
    """
    ## Introductions.
    print("Welcome! \n This program will calculate the sum of squares \n within a given range of numbers.")
    ## Obtain the input values from the user.
    start, end = eval(input("Please enter the range of numbers to be used \n separated by a comma. \n <Hit Enter to Continue>:"))
    ## Create the loop that will iterate through the range of numbers.
    result = 0
    for number in range(start, end):
        result = (number**2) + result
    squareResult = (end**2) + result
    ## Print the result.
    print("The summation of the range of squares is: \t", squareResult)
    

sumSquares()
    
def power():
    """
    Sadly, Phil the philosopher has found himself stranded on a deserted
    island with a bad version of Python that does not support the ** operator
    nor the math library function math.pow().  Phil needs to be able to
    calculate the power of numbers.  Write a function for him called power()
    that asks the user to input a base and an exponent. The function should
    use a loop to calculate and output the power.
    """
    ## Introducions.
    print("Hello! \n This program will calculate the power of a number provided by the user.")
    ## Establish variables for the root and the power it will be raised to.
    base, exponent = eval(input("Please input the value for the base and the exponent separated by commas. \n ( input = base, exponent ) \n <Hit Enter to Continue>:"))
    ## Create the loop that will calculate the result.
    result = 1
    for number in range(exponent):
        result = (result * base)
    ## Output the result.
    print("The result is: \t", result)

power()

def fibonacci():
    """
    A Fibonacci sequence is a sequence of numbers where each successive
    number is the sum of the previous two. The classic Fibonacci sequence
    begins: 0, 1, 1, 2, 3, 5, 8, 13, …. Write a function, fibonacci() ,
    that computes and outputs all of the Fibonacci numbers up to and
    including the nth number, where n is a value input by the user.
    """
    ## Introduction.
    print("Welcome! \n This program is designed to output the Fibonacci sequence \n to the nth value as designated by the user.")
    ## Obtain the user input for the nth value.
    n = eval(input("Please enter the amount of 'n' (steps in the sequence):"))
    ## Calculate the Fibonacci sequence.
    ## Define variables.
    result = 1
    fib1 = 0
    fib2 = 1
    for i in range(n):
        print(fib1)
        result = fib1 + fib2
        fib1 = fib2
        fib2 = result
    ## Output the result.
    if n == 0:
        print("The result will be: \n", fib1)
    elif n == 1:
        print("The result will be: \n", fib1)
    else:
        print("The result will be: \n", fib1)
    
fibonacci()

def newton():
    """
    Write a program, newton.py, that approximates the square root of a
    number using Sir Isaac Newton's method. Ask the user what the number,
    x, is and how many times to improve the approximation.  x / 2 is a
    good first approximation.
    """
    ## Introduction.
    print("Welcome! \n This program is designed to output the square root of a given number.")
    ## Obtain the user input for the value to find the root of.
    x = eval(input("Please enter the amount of 'x':"))
    ## Define variables.
    timesApproximation = eval(input("How many times would you like to improve the approximation?: "))
    ## Calculate the root.
    approx = 1
    for i in range(timesApproximation):
        approx = (((approx) + (x/approx))/2)
    ## Output the result.
    print(approx)

newton()

def pi():
    """
    Write a program "pi.py" that approximates the value of  using the
    Wallis formula on your sheet. The program should prompt the user for n,
    the number of terms in the series, compute the product of the n terms,
    and output the resulting approximation of pi.
    """
    ## Introduction.
    print("Welcome! \n This program is designed to compute the number of pi.")
    ## Obtain the user input for the value to find the root of.
    n = eval(input("Please enter the amount of 'n' (number of terms in the series):"))
    ## Calculate pi.
    piHalf = 1
    numerator = 0
    denominator = 1
    for i in range(n):
        denominator = denominator + (i%2)*2
        numerator = numerator + ((i+1)%2)*2
        piHalf = piHalf * (numerator/denominator)
    pi = piHalf * 2
    ## Output the result.
    print(pi)

pi()
