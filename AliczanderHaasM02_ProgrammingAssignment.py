# Aliczander Haas
# AliczanderHaasM02_ProgrammingAssignment
# Program generates a random number and the prompts for a guess
# Tells the user if the guess is too high/low and how many attempts it took once they guess correctly

import random  # Imports random number generator

secretNum = random.randint(1,10) #generates a random number between 1-100

print('Try and guess the secret number between 1-10')  # Tells the user the rules
numGuess = int(input('Guess here: '))  # Takes user input
guessCounter = 1  #Declares the amount of guesses made

while numGuess != secretNum:  #loops while users guess isn't the secret number

    if numGuess > secretNum:
        print('Too High, Try Again!')  # Tells user their guess is too high
        numGuess = int(input('Guess again here: '))  # Takes repeated guess inputs
        guessCounter = guessCounter + 1  # Increments the number of guesses made by one

    if numGuess < secretNum:
        print('Too Low, Try Again!')  # Telss the user their guess is too low
        numGuess = int(input('Guess again here: '))  # Takes repeated user inputs
        guessCounter = guessCounter + 1  # Increments the number of guesses made byh= one

else:
    print('You Guessed The Secret Number!')  # Congrats message
    print('And it only took you ' + str(guessCounter) + ' tries!')  #Try counter message