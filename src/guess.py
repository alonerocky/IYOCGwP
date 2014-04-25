'''
Created on Mar 21, 2014

@author: shoulongli
'''

import random
print('What is your name ?')
player = input()
print('Hello ')
print('This is the guess game')
print('I will generate one number and you will try to guess it out in 6 times')

guessed = 0
number = random.randint(1,30)
print("number : "+str(number))
while guessed < 6 :
    print('what is your guess ?')
    guess = int(input())
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else :
        break
    guessed = guessed + 1

if(guess == number):
    print("good job! you guessed my number "+str(number)+" in "+str(guessed)+" times")
else :
    print("you didn't guess it , my number is "+str(number))




