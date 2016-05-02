## hangman.py
##
## Name : Jake Hennessy
## Date : 3.31.14
## Class : CSCI 220/L
## Prof : Stalvey
##
## Certification of Authenticity:
##      I certify that this lab is my own work.
##
## Purpose :
##      This program is designed to open and read an external text file that
##    will contain a series of words that will then be used with a program that
##    will display a game of hangman represented graphically that will change
##    based on the user's input.
##      The program will use a series of defined functions to allow gameplay
##    which will primarily involve interating through a list of letters that
##    spell the secret word, and other lists that will contain letters that
##    have already been guessed.
##        The program will also contain conditionals that will change the flow
##    of the game, and once again all changes and necessary user interaction
##    will occur on the graphics window.
##      Essentially, the program will be a synthesis of the previous chapters
##    we have studied and putting this all together.

## Importing various libraries that will be used within this program.

from graphics import *
from random import *
import time

## Defining the function that will read the wordlist.txt file

def readWordlist(filename):
    
    ## Opening the .txt file and reading
    infile = open(filename, 'r')
    
    ## Creation of list object that will contain the words read in the file
    wordlist = []
    
    ## For loop that will append words to list.
    for line in infile:
        ## This conditional removes carriage returns for correct len(word)
        if ((line[-1]) == '\n'):
            line = line[:-1]
            lowerLine = line.lower()
            wordlist.append(lowerLine)
        ## else condition only applies to last item in list!!
        else:
            lowerLine = line.lower()
            wordlist.append(lowerLine)
    return wordlist



## Create the function that will select a random word from the wordlist.

def selectWord(listObject):
    
    ## Determining the index position to accesss in the list using
    ##  the randint(start, stop) method.
    randomIndex = randint(1, len(listObject))
    
    ## accessing the list at the specified position
    guessWord = listObject[randomIndex]
    return guessWord



## Creating a function that will take the secret word and turn it
##      into a list of its letters.

def breakUpWord(word):
    ## Creating an empty list to hold letters
    letters = []
    
    ## Create a loop that will split the words and append to the empty list above
    for letter in word:
        letters.append(letter)
    return letters


## Creating a function to present the user with a prompt that will allow
##  the user to play another game of hangman.

def anotherGame():

    ## Initializing variables
    continuePrompt = ''
    
    ## Creeating a list of accepted responses.
    legalValues = ['y', 'Y', 'yes', 'Yes', 'n', 'N', 'No', 'no']

    ## Creating conditions for the prompt to loop until good input is reached.
    while continuePrompt not in legalValues:
        ## Presnting the user with a prompt for input
        continuePrompt = input('\n\tWould you like to play another game?\n\t<<<Yes or No>>>: ')
        ## Creating conditions that allow for another game.
        if continuePrompt in legalValues:
            if continuePrompt in legalValues[0:4]:
                return True
            elif continuePrompt in legalValues[4:]:
                return False



## Defining a function to create buttons

def createButton(anchorPoint, textString):
    # Using parameters above, we will create a standard button.
    button = Rectangle((anchorPoint), (Point((anchorPoint.getX() + 80), (anchorPoint.getY() + 50))))
    # Cloning button to create a shadow effect
    buttonShadow = button.clone()
    # Setting button styles
    button.setOutline('white')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    # Setting shadow styles
    buttonShadow.setFill('black')
    buttonShadow.move(3, 3)
    # Setting button text style
    buttonText = Text((button.getCenter()), (textString))
    buttonText.setTextColor('white')
    buttonText.setFace('helvetica')
    # return the various objects
    return button, buttonText, buttonShadow

## Creating an animate button function.

def animateButton(button, buttonText):
    ## moving the upper button to appear 'clicked'
    button.move(3, 3)
    buttonText.move(3, 3)
    ## Changing the styles of the button when 'clicked'
    buttonText.setStyle('bold')
    button.setWidth(4)
    button.setFill(color_rgb(255, 99, 71))
    ## Pause
    time.sleep(.5)
    ## Undo the above changes, to make button appear to 'pop back out'
    button.move(-3, -3)
    buttonText.move(-3, -3)
    buttonText.setStyle('normal')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    return



## Defining the function that will check whether the letters entered
##      spell the secret word.

def letterCheck(letterGuessed, secretWord):

    ## Condition that ensures only one letter will be accepted.
    while len(letterGuessed) == 1:
        ## Condition that checks if the guessed letter is in the secret word
        if letterGuessed in secretWord:
            return True
        elif letterGuessed not in secretWord:
            return False



##  A function that returns the “guessed” word at a given point.
##      (E.g.  If the word is “slant” and the user has guessed the letters ‘t’
##      and ‘a’, this function should return “_ _ a _ t”)

def wordStatus(userGuess, lettersGuessed, blanks, secretWord, guessCount):

    ## Initializing a variable to only provide 7 guesses
    tooManyGuesses = 7
    
    ## Conditionals to check on the status of the word.
    ## First we intialize an object that the function returns its value to
    guessTF = letterCheck(userGuess, secretWord)
    
    ## Conditions that control game flow based on whether the user has guessed
    ##  correctly.
    if guessTF == True:
        ## For loop that iterates through the letters in the secretWord
        for i in range(len(secretWord)):
            ## Condition that will be met if the letter[i] from the loop matches
            ##  the user's guess
            if userGuess == secretWord[i]:
                ## Slicing the string to insert the secret letter at index [i]
                blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
        ##  
        if (blanks == secretWord):
            print('\nYou Win!\n You saved the hangman with', (tooManyGuesses - guessCount), 'guesses to spare!')
    elif guessTF == False:
        guessCount += 1
        if guessCount == tooManyGuesses:
            lettersGuessed.append(userGuess)
            print('\nYou Lose!!\n\t The word was:', secretWord)
        else:
            lettersGuessed.append(userGuess)
            print('\n\tSorry! \'', userGuess,'\' is not in the word!\n')
            print('\t That was wrong guess #', guessCount)
            print('\t Only', (tooManyGuesses - guessCount), 'guess(es) left!!\n')
    return blanks, guessCount, lettersGuessed



def formatOutput(textString):
    textReFormat = ''
    for ch in textString:
        textReFormat += ch + ' '
    return textReFormat



## Defining the function that will control and allow the user to play hangman

def hangman(infileName):
    
    ## Creating the wordlist from the readWordlist() function defined earlier.
    wordlist = readWordlist(infileName)

    ## Create the graphics window to start the game!
    win = GraphWin('<<<<<<   HANGMAN   >>>>>>', 600, 600)
    win.setBackground('light sea green')

    ## Create the text that will go in the graphics window.
    hangmanTitle = Text(Point((win.getWidth() * .5), (win.getHeight() * .1)), 'HANGMAN')
    hangmanText, hangmanShadow = setTextStyle(hangmanTitle, 36, 'white', 'bold italic')
    hangmanShadow.draw(win)
    hangmanText.draw(win)
    
    ## Obtain a secret word from the wordlist provided in the .txt file
    secretWord = selectWord(wordlist)
    
    ## Creating an empty list to hold letters that are NOT in the word
    lettersGuessed = []
    blanks = '_' * (len(secretWord))
    print('Secret Word: \n')
    for letter in blanks:
        print(letter, end = ' ')
    print('\n\n##################################\n')
    
    ## Creating variable to count the number of guesses
    guessCount = 0
    tooManyGuesses = 7

## =========== Creating the graphics portion of the program. ==============
    ## Creating Text that will dipsly the words and wrong guesses
    blanksGraphic = Text(Point(win.getWidth() * .5, (win.getHeight() * .2)), ('_ ') * len(secretWord))
    blanksText, blanksShadow = setTextStyle(blanksGraphic, 36, 'white', 'bold italic')
    blanksShadow.draw(win)
    blanksText.draw(win)

    ## Creating a text entry box that will allow for letters to be guessed
    guessBox = Entry(Point(win.getWidth()/2, win.getHeight() * (9.2/10)), 40)
    guessBox.setStyle('bold')
    guessBox.draw(win)

    ## Creating more text
    enterALetter = Text(Point(win.getWidth() * (1/6), (win.getHeight() * (9/10))), 'Enter a\nLetter:')
    enterText, enterShadow = setTextStyle(enterALetter, 24, 'tomato', 'bold italic')
    enterShadow.draw(win)
    enterText.draw(win)

    ## Creating text that will be next to the wrong letters.
    wrongLetters = Text(Point(win.getWidth() * (1/6), (win.getHeight() * (8/10))), 'Wrong\nLetters:')
    wrongText, wrongShadow = setTextStyle(wrongLetters, 24, 'spring green', 'bold italic')
    wrongShadow.draw(win)
    wrongText.draw(win)

    ## Creating the empty block that will disply the wrong letters
    wrongGuesses = Text(Point(win.getWidth() * (3/6), (win.getHeight() * (8/10))), '')
    wrongGuessesText, wrongGuessesShadow = setTextStyle(wrongGuesses, 24, 'spring green', 'bold italic')
    wrongGuessesShadow.draw(win)
    wrongGuessesText.draw(win)

    ## Creating the graphic text that will be above the guesses left
    guessesLeft = Text(Point(win.getWidth() * (9/10), (win.getHeight() * (3.5/10))), 'Guesses\nLeft!')
    guessesLeftText, guessesLeftShadow = setTextStyle(guessesLeft, 20, 'lavender', 'bold italic')
    guessesLeftShadow.draw(win)
    guessesLeftText.draw(win)

    ## Creating the graphic text that will display the guesses left
    guessesCount = Text(Point(win.getWidth() * (9/10), (win.getHeight() * (4.5/10))), (tooManyGuesses))
    guessesCountText, guessesCountShadow = setTextStyle(guessesCount, 36, color_rgb(253, 87, 40), 'bold')
    guessesCountShadow.draw(win)
    guessesCountText.draw(win)

    ## Creating a button for the user to click to submit a letter.
    guessBttn, guessBttnText, guessBttnShadow = createButton(Point(win.getWidth() * (7.5/10), win.getHeight() * (8.5/10)), 'Make\nGuess')
    guessBttnShadow.draw(win)
    guessBttn.draw(win)
    guessBttnText.draw(win)
    
    ## Creating the loop to control the game flow
    while (blanks != secretWord) and (guessCount < tooManyGuesses):
        ## Obtaining user input
        point = win.getMouse()
        if point.getX() > (win.getWidth() * .75) and point.getX() < ((win.getWidth() * .75) + 80) and point.getY() > (win.getHeight() * .85) and point.getY() < ((win.getHeight() * .85) + 50):
            animateButton(guessBttn, guessBttnText)
            userGuess = guessBox.getText()
            guessBox.setText('')
            print(userGuess)
            if len(userGuess) != 1:
                print('Please enter only 1 letter.')
            elif userGuess in lettersGuessed or userGuess in blanks:
                print('The letter \'', userGuess, '\' has already been guessed. Try again!')
            elif userGuess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter lowercase letters only. Try again!')
            elif blanks == secretWord or guessCount >= tooManyGuesses:
                print('\n\n##################################\n')
            else:
                blanks, guessCount, lettersGuessed = wordStatus(userGuess, lettersGuessed, blanks, secretWord, guessCount)
                graphBlanks = formatOutput(blanks)
                graphWrongGuess = formatOutput(lettersGuessed)
                guessesCountShadow.setText(tooManyGuesses - guessCount)
                guessesCountText.setText(tooManyGuesses - guessCount)
                wrongGuessesShadow.setText(graphWrongGuess)
                wrongGuessesText.setText(graphWrongGuess)
                blanksShadow.setText(graphBlanks)
                blanksText.setText(graphBlanks)
                print('\nSecret Word:\n')
                for letter in blanks: 
                    print(letter, end=' ')
                print('\n')
                print('Wrong letters:', end=' ')
                for letter in lettersGuessed:
                    print(letter, end=' ')
                print('\n\n##################################\n')
    blanksShadow.undraw()
    blanksText.undraw()
    hangmanShadow.undraw()
    enterShadow.undraw()
    enterText.undraw()
    wrongShadow.undraw()
    wrongText.undraw()
    wrongGuessesShadow.undraw()
    wrongGuessesText.undraw()
    guessesLeftShadow.undraw()
    guessesLeftText.undraw()
    guessesCountShadow.undraw()
    guessesCountText.undraw()
    guessBttnShadow.undraw()
    guessBttnText.undraw()
    guessBttn.undraw()
    guessBox.undraw()
    hangmanText.setText('Play Again?')
    win.getMouse()
    win.close()


## Creating a function to produce buttons.

def createButton(anchorPoint, textString):
    ## Using parameters above, we will create a standard button.
    button = Rectangle((anchorPoint), (Point((anchorPoint.getX() + 80), (anchorPoint.getY() + 50))))
    ## Cloning button to create a shadow effect
    buttonShadow = button.clone()
    ## Setting button styles
    button.setOutline('white')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    ## Setting shadow styles
    buttonShadow.setFill('black')
    buttonShadow.move(3, 3)
    ## Setting button text style
    buttonText = Text((button.getCenter()), (textString))
    buttonText.setTextColor('white')
    buttonText.setFace('helvetica')
    ## return the various objects
    return button, buttonText, buttonShadow

## Create an animate button function.

def animateButton(button, buttonText):
    ## moving the upper button to appear 'clicked'
    button.move(3, 3)
    buttonText.move(3, 3)
    ## Changing the styles of the button when 'clicked'
    buttonText.setStyle('bold')
    button.setWidth(4)
    button.setFill(color_rgb(255, 99, 71))
    ## Pause
    time.sleep(.5)
    ## Undo the above changes, to make button appear to 'pop back out'
    button.move(-3, -3)
    buttonText.move(-3, -3)
    buttonText.setStyle('normal')
    button.setWidth(2)
    button.setFill(color_rgb(100, 149, 237))
    return

## Define a function to style the text on the window in a similar manner.

def setTextStyle(textObject, size, textColor, style):
    textObject.setFace('courier')
    textObject.setStyle(style)
    textObject.setSize(size)
    textShadow = textObject.clone()
    textShadow.move(2, 2)
    textObject.setTextColor(textColor)
    textShadow.setTextColor('black')
    return textObject, textShadow

    
## Defining the main function.

def main():
    
    ## Using text blocks to give the user an intro!
    print('\t##################################')
    print('\t#--------------------------------#')
    print('\t#<<<<<<   H A N G M A N   >>>>>>>#')
    print('\t#--------------------------------#')
    print('\t##################################\n')
    print('\tLet\'s Play a Game -- of HANGMAN!\n')

    ## Obtaining input to start the game
    enterCommand = input('\t <<< Hit Enter to Start >>> \n')
    
    ## Obtaining the name of the file from the user.
    print('\tFirst, what is the name of the file? \n\t   < With .txt Extension >\n')
    infileName = input('\tFilename: ')
    print()
    hangman(infileName)

    ## If game is over, present user with the option to play again.
    while True:
        anotherPrompt = anotherGame()
        if anotherPrompt == True:
            print('\n')
            hangman(infileName)
        elif anotherPrompt == False:
            print('\n\n##################################\n')
            print('Thanks for Playing!')


main()
