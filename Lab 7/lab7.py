# Lab7.py
# Name 1: Jake Hennessy
# Name 2: Scott Sandie

def formatPractice(): 
    """
    Each print statement contains a variable enclosed in angle brackets.
    Replace the variables (including the brackets) with code so that the
    three statements print the output given below:
    """

    print("It’s raining {1} and {0}.".format("dogs", "cats"))
    #expected output:
    #It's raining cats and dogs

    print("{0:0.2f} {1:0.3f}".format(2.3, .4567))
    #expected output:
    #2.30 0.457

    print("Time left {0:02}:{1:05.2f}".format(3, 3.4589))
    #expected output:
    #Time left 03:37.46


formatPractice()
    

def pigLatin():
    """
    This function that reads in a sentence and converts it to a 
    simplified form of pig Latin.
    """
    sentence = input("Please enter a sentence: ")
    # Take the sentence and make it all one case
    string = sentence.lower()
    # Split the string to be able to access the individual words in a list
    words = string.split()
    # Loop to 
    for word in (words):
        # Determine the length of the word being processed
        length = len(word)
        # Access the first letter of each word to be able to manipulate
        firstLetter = word[0]
        # Output the result by shifting around the letters
        print(word[1:length] + (firstLetter) + "ay" + " ", end="")
    



pigLatin()

    
def numberWords():
    """
    This function reads the contents of a text file, numbers each word,
    and writes the number and the word to the output file. 
    """
    # Designate file to open, and that it will be read
    infileName = "rawWords.txt"
    infile = open(infileName, "r")

    # Designate the file to write to.
    outfileName = "numberedWords.txt"
    outfile = open(outfileName, "w")

    # Creating a list to hold all of the words to be processed on all lines
    totalWordList = []
    # Loop to split each line
    for line in infile:
        wordList = line.split()
        # Adding each list from each line to the main list
        totalWordList += wordList
        # Opposite solution!
        """for word in wordList:
            totalWordList.append(word)"""
    # Starting a count to create a numbered list
    count = 0
    # Loop to advance count, and print its corresponding word
    for word in totalWordList:
        count += 1
        # outputting the data to the output file
        print((count),".", (word), file = outfile)

    # Printing a line in the shell that lets user knows the output file is done
    print("\nThe files have been processed.")
    # Closing the output file
    outfile.close()

    


numberWords()

    
def hourlyWages():
    """
    This function reads a file of employee data and calculates each
    employee’s new pay for the week, given a specified raise. 
    """
    # Designate file to open, and that it will be read
    infileName = "hourlyWages.txt"
    infile = open(infileName, "r")
    
    # Designate the file to write to.
    outfileName = "newHourlyWages.txt"
    outfile = open(outfileName, "w")

    # Loop to spli each line in the text file
    for line in infile:
        splitLine = line.split()
        # eval'ing the pay rate and creating the new rate
        newRate = eval(splitLine[2]) + 1.65
        # calculating the pay for the week
        weeklyPay = eval(splitLine[3]) * newRate
        # Formatting the output in the outfile
        print(splitLine[0] + " " + splitLine[1] + "'s new wage: {0:.2f}".format(newRate), file = outfile)
        print("\t" + splitLine[0] + " " + splitLine[1] + "'s hours this week:", (splitLine[3]), "hours.", file = outfile)
        print("\t" + splitLine[0] + " " + splitLine[1] + "'s pay this week: {0:.2f}".format(weeklyPay), file = outfile)
    # Letting the user know that the files are finished writing
    print("\nThe files have been processed.")




hourlyWages()


def encode():
    """
    This function encodes a simple Caesar cipher (positional cipher).
    """
    # Obtain the user input
    string = input("Please enter a sentence to encode: ")
    # Make the string all the same case of character
    lowerString = string.lower()
    # Obtain the amount of shift in the cipher
    key = eval(input("Please enter the key for the cipher: "))
    # Loop
    for ch in lowerString:
        # Converting each character to ascii value
        convert = ord(ch)
        # adding the shift to the ascii value
        new = convert + key
        # converting back to characters
        code = chr(new)
        # Printing each letter on the same line
        print(code, end="")
    print()



encode()


def encodeBetter():
    """
    This function encodes a better Caesar cipher that avoids the
    problem of “drop[ping] off the end” of the alphabet. 
    """
    userInput = input("Please enter a sentence to encode: ")
    # Make the string lowercase to use the cipher
    userString = userInput.lower()
    # Obtain the key (number of letters to shift in the alphabet)
    key = eval(input("Please enter the key for the cipher: "))
    # Loop to access each letter and encode it
    for ch in userString:
        # This line takes one letter, encodes it to ascii, and subtracts 97
        #   to shift the range of alphabet from 0-25.
        #   The modulo allows for the remainder of each encoded letter to
        #   "wrap around" to the beginning of the alphabet
        convert = ((ord(ch) - 97) + key) % 26
        # Here we add back the 97 to get the actual ascii value of each letter
        new = (convert) + 97
        # using chr() to get the ascii value back to a character
        code = chr(new)
        # printing each letter on the same line.
        print(code, end="")
    print()


encodeBetter()



    
