# SimpleDifference.py
# CSCI 220 - Lab 01 - 1/13/14
# Author: Jake Hennessy
#
# Purpose: This program will calculate the difference of two numbers.

# Define the main function.
def main():
    # Introductions.
    print("Welcome!")
    print("This program will calculate the difference of two numbers.")
    # Obtain the numbers to be used in calculation.
    num1 = eval(input("What is the first number to be used?: "))
    num2 = eval(input("What is the second number that will be used?: "))
    # Perform the calculation.
    difference = num1 - num2
    # Output the result
    print("The difference is", difference)

main()
