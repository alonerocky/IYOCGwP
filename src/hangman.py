'''
Created on Mar 24, 2014

@author: shoulongli
'''
import random
VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
HANGMANPICS = [
               '''

  +---+
  |   |
      |
      |
      |
      |
=========
               ''',
               '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
               ''',
               '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
               ''',
               '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
               ''',
               '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
               ''',
               '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
               ''',
               '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
               '''
               ]
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot
pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth
snake spider stork swan tiger toad trout turkey turtle weasel whale wolf
wombat zebra'''.split()


def getRandomWord(words):
    wordIndex = random.randint(0,len(words)-1)
    return words[wordIndex]

def displayBoard(HANMANPICS,missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print("Missed letters: ")
    for ch in missedLetters:
        print(ch, end= ' ')
    print()
    blanks = '*' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter , end = ' ')
    print()

def playAgain():
    print('do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def getGuess(alreadyGuessed):
    while True:
        print('Guess one letter:')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in VALID_LETTERS:
            print('Please enter a LETTER.')
        else:
            return guess
def main():
    print('H A N G M A N ')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameOver = False
    while not gameOver:
        displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord);
        guess = getGuess(missedLetters + correctLetters)
        if guess in secretWord:
            correctLetters = correctLetters + guess
            foundAll = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAll = False
                    break

            if foundAll:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameOver = True

        else:
            missedLetters = missedLetters + guess
            if len(missedLetters) == len(HANGMANPICS) -1:
                displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
                print('Your have run out of guesses!\n After '+str(len(missedLetters)) +
                      'missed guesses and '+str(len(correctLetters)) +' correct letters '+
                      ' the secret word was '+secretWord);
                gameOver = True;

        if gameOver:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameOver = False
                secretWord = getRandomWord(words)
            else:
                break

main()