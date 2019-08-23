#coding challenges

#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

#while loop
i = 0
while i < 3:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess) # converts a string to an integer
        if int(guess) > aRandomNumber and i != 2:
            print("Your guess was larger than the secret number! Try again!")
        if int(guess) < aRandomNumber and i != 2:
            print("Your guess was smaller than the secret number! Try again!")
        if int(guess) == aRandomNumber:
            print("You were right! Congrats!")
            i = 3
        if int(guess) != aRandomNumber and i == 2:
            print("Sorry, you're out of guesses! Better luck next time!")
        i += 1
restart = input()
if restart == "play again":
    i = 0
