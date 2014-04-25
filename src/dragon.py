'''
Created on Mar 23, 2014

@author: shoulongli
'''
import time
import random

def mainloop():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)
        print('Do you want to play again? (yes or no)')
        playAgain = input()

def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyDragon = random.randint(1,2)
    print('dragon in '+str(friendlyDragon))
    print(str(chosenCave == friendlyDragon))
    if int(chosenCave) == friendlyDragon:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


mainloop()



