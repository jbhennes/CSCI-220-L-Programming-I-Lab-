# CSCI 220L - Lab 10 Solutions
#
# Name 1: Sami Williams
#
# Name 2: Jake Hennessy

from random import *

def calculateSum(value, numIterations):
    i = 0
    total = 0
    while i < numIterations:
        total += value
        i += 1
    return total

def areEqual(num1, num2):
    if (abs(num1 - num2) <= (.0001))  :
        answer = True
    else:
        answer = False

    return answer


def main():
    value = eval(input("input a value to calculate: "))
    numIterations = eval(input("input number of times to iterate: "))
    total = calculateSum(value, numIterations)
    print("THE total is", round(total, 4))
    result =calculateSum(.1, 10)
    print('The result of .1 * 10 is:', result)
    equals = areEqual(1.0, result)
    if equals == True:
        print("YAY! They are equal!!")
    else:
        print("NAY! They are not equal!!")

    numRange = goodInput()
    print (numRange)
    hiLoGame()
    numDigits()

    
    


def goodInput():
    numRange = eval(input("Input a number between 1 and 10: "))
    while numRange > 10 or numRange < 1:
        print ("The number was not in range. Try again. BETWEEN 1 & 10")
        numRange = eval(input("Input a number between 1 and 10: "))
    return numRange

def numDigits():
    integer = eval(input('Enter that there positive integer, bub: '))
    count = 0
    while integer > 0:
        count = 0
        while (integer > 0):
            integer = integer//10
            count +=1
        print('the numero de numeros es', count)
        integer = eval(input('Enter that there positive integer, bub: '))

def hiLoGame():
    num = randint(1, 100)
    count = 0
    numGuess = eval(input("Guess a number: "))
    
    while count < 6 and numGuess != num:
        if numGuess > num:
            print ("Too high!")
            count += 1
            numGuess = eval(input("Guess a number: "))
        elif numGuess < num:
            print ("Too low!")
            count += 1
            numGuess = eval(input("Guess a number: "))
    if numGuess == num:
        print ("Correct!")
        print ("You win in", count + 1, "guesses.")
    elif count == 6:
        print ("Sorry, you lose. The number was", num)
        

numDigits()
