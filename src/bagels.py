'''
Created on Apr 18, 2014

@author: sli1
'''
import random

NUMDIGITS = 3
MAXGUESS = 10

def printIntroduction():
    print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
    print('Here are some clues:')
    print('When I say:    That means:')
    print('  Pico         One digit is correct but in the wrong position.')
    print('  Fermi        One digit is correct and in the right position.')
    print('  Bagels       No digit is correct.')

def getSecretNumber(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNumber = ''
    for i in range(numDigits):
        secretNumber += str(numbers[i])
    return secretNumber

def isOnlyDigits(number):
    if number == '':
        return False
    for i in number:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def getClues(guess, secretNumber):
    if guess == secretNumber:
        return "you got it!"

    clue= []
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clue.append('Fermi')
        elif guess[i] in secretNumber:
            clue.append('Pico')

    if len(clue) == 0:
        return 'Bagels'

    clue.sort( )
    return ' '.join(clue)


def playAgain():
    print("Do you want to play again ? (yes or no)")
    return input().lower().startswith('y')


def mainloop():
    while True:
        secretNumber = getSecretNumber(NUMDIGITS)
        print('I have thought up one number and you have %s guesses to get it' % (MAXGUESS))

        numOfGuess = 1
        while numOfGuess < MAXGUESS:
            guess = ''
            while len(guess) != NUMDIGITS or not isOnlyDigits(guess) :
                print('Guess #%s' %(numOfGuess))
                guess = input()

            clue = getClues(guess,secretNumber)
            print(clue)
            numOfGuess += 1
            if guess == secretNumber:
                break;
            elif numOfGuess > MAXGUESS:
                print('you ran out of guesses ,the number was: %s' %(secretNumber))

        if not playAgain():
            break;

mainloop()
