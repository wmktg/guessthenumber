# this is a guess the number game

import random 
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# ask the player to guess 6 times

for guessesTaken in range (1,7):
    print('Take a guess.')
    guess = int(input())