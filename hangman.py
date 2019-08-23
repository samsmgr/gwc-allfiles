#create a list of words
#word=random word from list of possible words
#make an list of dashes/ revealed letters (one for each letter of the word)
#make a list of gussed letters
#keep track of number lives left
#keep track of number of unguessed letters
#while number of lives !=0 and number of unguessed letters !=0 then
#A. print list of of dashes/revealed letters (to represent the dashes and guessed letters)
#B. print the current list of guesses
#C. print the number of lives left
#D. guess= input ("Guess a letter")
#E. if guess is valid (AKA 1 letter)then
#I. if the letter is in the word then
#1. update the dashes with letters for each correct guess.
#2.Subtract 1 from number of unguessed letters
#ii. elif the letter is not in the word
#1. remove a life
# 2. add guess to list of guesses
#F. else
#i. print ("invalid input. guess again")
#  if number of ungusses letters== 0 then
#i. print (you won!)
# elif number of lives left == 0 then
#i print (you lost!)
from random import *

choice = input("Single-player mode or multi-player mode? (1 or 2) ")

if choice == "1":
    whichword = randint(0,2)
    words = ["INCREDIBLE", "VARIOUS", "TELETUBBY", "DEBUGGING", "INSENSIBLE"]
    guessletters= []
    lives = 6
    x = 0
    underscores = []
    secretword = words[whichword]
    while x < len(secretword):
        underscores.append("_")
        x += 1

    print(underscores)
    print("Guess a letter!")
    while lives != 0 and "_" in underscores:
        print ("GUESSED LETTERS: " + str(guessletters))
        guess = input()
        if guess.upper() in guessletters:
            print("You already guessed that letter! Try again:")
        elif len(guess) != 1:
            print("Sorry, that's not a valid guess. Try again: ")
        elif guess.upper() in words[whichword] :
            print("That's correct! Guess another:")
            guessletters.append(guess.upper())
            for y in range(len(words[whichword])):
                if words[whichword][y] == guess.upper():
                    underscores[y] = guess.upper()
            print(underscores)
        else:
            lives -= 1
            print("Uh oh... that's not correct! You have " + str(lives) + " lives left. Try again:")
            guessletters.append(guess.upper())
            print(underscores)

    if lives == 0:
        print("YOU LOSE!! YOUR WORD WAS: " + str(secretword))

    if "_" not in underscores:
        print("YOU WIN!!")

if choice == "2":
    word = input("Player 1, please enter the secret word: ").upper()
    for z in range(30):
        print()
    guessletters= []
    lives = 6
    x = 0
    underscores = []
    while x < len(word):
        underscores.append("_")
        x += 1

    print(underscores)
    print("Player 2, please guess a letter!")
    while lives != 0 and "_" in underscores:
        print ("GUESSED LETTERS: " + str(guessletters))
        guess = input()
        if guess.upper() in guessletters:
            print("You already guessed that letter! Try again:")
        elif guess.upper() in word:
            print("That's correct! Guess another:")
            guessletters.append(guess.upper())
            for y in range(len(word)):
                if word[y] == guess.upper():
                    underscores[y] = guess.upper()
            print(underscores)
        else:
            lives -= 1
            print("Uh oh... that's not correct! You have " + str(lives) + " lives left. Try again:")
            guessletters.append(guess.upper())
            print(underscores)

    if lives == 0:
        print("YOU LOSE!! YOUR WORD WAS: " + str(word))

    if "_" not in underscores:
        print("YOU WIN!!")
