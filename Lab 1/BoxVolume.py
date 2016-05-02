# BoxVolume.py
# CSCI 220 - Lab 01 - 1/13/14
# Author: Jake Hennessy
#
# The purpose of this program is to calculate the volume of rectangular solid.

def boxVolume():
    print("This program calculates the volume of a rectangular prism.")
    print()

    length = eval(input("Please enter the length: "))
    width = eval(input("Please enter the width: "))
    height = eval(input("Please enter the height: "))

    area = length * width * height

    print("Area =", area, "units cubed.")

def main():
    boxVolume()

main()
