# Lab6.py
#
# Name 1: Scott Sandie
# Name 2: Jake Hennessy
#
# Date: 2.17.14

def nameReverse():
    name = input("Please type the first and last name: ")
    lastName = name.split()[1]
    firstName = name.split()[0]
    print((lastName), ",", (firstName))
    
#nameReverse()
    


def companyName():
    domain = input("Please enter the web address of a company: ")
    company = domain.split(".")[1]
    print(company)

#companyName()


def initials():
    students = eval(input("How many students would you like to process? "))
    print()
    for student in range(students):
        fName = input("Please enter the student's first name: ")
        lName = input("Please enter " + (fName) + "'s last name: ")
        firstInit = fName[0] + "."
        lastInit = lName[0] + "."
        print()
        print((fName) + "'s initials are", (firstInit) + (lastInit))
        print()
        """Below is another solution to this problem!"""
##        name = input("Please enter the student's first and last name: ")
        """The next line will create a list, dividing items by spaces in between."""
##        fullName = name.split()
        """The next line is structured like this:
 newVariable = listObject[indexPos][indexPosWithinItem].method() + concat"""
##        firstInit = fullName[0][0].upper() + "."
##        lastInit = fullName[1][0].upper() + "."
##        print()
##        print((firstInit) + (lastInit))
##        print()
        

#initials()


def names():
    mainNames = input("Please enter the first and last names of a few people, separated with commas: ")
    print()
    fullNames = mainNames.split(",")
    for name in fullNames:
        person = name.split()
        firstName = person[0][0].upper() + "."
        lastName = person[1][0].upper() + "."
        """Below is another solution to the same problem!"""
##        for letter in person:
##            initial = letter[0:1]
##            print(initial.upper() + ". ", end="")
        print(firstName, lastName)
        
   
#names()


def thirds():
    sentences = eval(input("How many sentences would you like to type? "))
    print()
    for i in range(sentences):
        line = input("Please type your sentence: ")
        print()
        # The next line is structured like this:
        #   newVariable = object[startIndex : stopIndex : stepAmount]
        thirdLetter = line[2::3]
        print(thirdLetter)
    
#thirds()


def wordCount():
    howMany = eval(input("How many sentences would you like to count?"))
    finalNumWords = 0
    for i in range(howMany):
        sentence = input("Please type a sentence: ")
        words = sentence.split()
        totalWords = len(words)
        print("The number of words in this sentence is: ", (totalWords))
        finalNumWords = totalWords + finalNumWords
    print("The total tally of all sentences is: ", (finalNumWords))
        
#wordCount()


def wordAverage():
    sentences = eval(input("How many sentences would you like to average? "))
    wordLength = []
    totalWordAverage = 0
    print()
    for i in range(sentences):
        sentence = input("Please enter your sentence: ")
        print()
        wordSplit = sentence.split()
        for word in (wordSplit):
            numCharacter = len(word)
            wordLength.append(numCharacter)
        wordLengthAverage = sum(wordLength) / len(wordLength)
        totalWordAverage = totalWordAverage + wordLengthAverage
        print("The average word length is:", (wordLengthAverage))
        print()
    print("The average word length of all sentences is:", (totalWordAverage))
            
       
        
#wordAverage()


def gradeToLetter():
    numGrade = eval(input("Please enter the numeric grade: "))
    # Using a string with 11 characters, we then can find the grade at
    #   various positions.
    gradeStr = "FFFFFFDCBAA"
    # Using integer division, we can get a value to use as an index position
    listPos = numGrade//10
    totalGrade = gradeStr[listPos]
    print("\tThe letter grade is:", (totalGrade))
    
   
   
#gradeToLetter()

