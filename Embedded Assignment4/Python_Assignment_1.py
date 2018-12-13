#!bin/user/python3

#Hangman

#Using the python program structure outlined in the lectures, create a hangman game for the user.
#The program randomly selects a word from a list and tell the user how many letters are in the word they have to guess.
#You are to ask the user to guess the letters contained within the word.
#You will need functions to check if the user has actually inputted a single letter,
#to check if the inputted letter is in the hidden word (and if it is, how many times it appears),
#to print letters, and a counter variable to limit guesses (num guesses should be set a size of word minus 1).

#For example, if the random word a user had to guess was LINUX then the program might work as follows:
#> Guess either the letters in this 5 letter word or the word itself (you have 4 letter guesses):
#> L
#> Yes, the letter L appears in this 5 letter (L _ _ _ _) word (you have 3 letter guesses remaining):
#> V
#> No, the letter V does not appear in the word (you have 2 letterguesses remaining):
#> I
#> Yes, the letter I appears in this 5 letter (L I _ _ _) word (you have 1 guesses remaining):
#> LANES
#> No, the word is not LANES. Please try again you have 1 letter guess remaining):
#> X
#> Yes, the letter X appears in this 5 letter (L I _ _X) word (you have 0 guesses remaining but you have unlimited guesses for the word):
#> LINEX
#> No, the word is not LINEX. Please try again, you have unlimited guesses for the word):
#> LINUX
#> Yes, congrats you correctly guessed the word.

import random

#Main method that calls the hangman method which takes in the final word from
#the random method.
def main():
  makeGuess(randomWord())


#Method that pulls in words from a file with 500 randomly generated words.
#The words are added to an array, where one is chosen at random. This word
#is passed into the hangman method as the word the player is trying to guess.
def randomWord():

  wordFile = open("words.txt", "r")
  wordArray = []
  for line in wordFile:
      wordArray.append(line.upper())
  word = random.choice(wordArray)
  return word


#Method that runs the actual game of hangman.
#The word that is taken in, has each of its letters put in an array,
# such that checking for correctly guessed letters is much easier.
def makeGuess(word):
    print("")
    print("You have 7 guesses left!")
    guessesLeft = 7
    wordProgress = []
    i = 0
    while i < len(word):
        wordProgress.append("_")
        i+=1
    wordProgress.pop()
    print(wordProgress)
    while guessesLeft !=0:
        inputLetter = input("Guess a letter in the word! Your guess: ").upper()
        if str(inputLetter) in word:
            x = 0
            while x < len(word):
                if word[x:x+1] == inputLetter:
                    wordProgress[x] = inputLetter
                x +=1
            print(wordProgress)
            if "_" not in wordProgress:
                print("Congratulations! You guessed the word! The word was" +word)
                print("")
                answer = input("Would you like to play again? (Y/N)")
                if answer == "y" or answer == "Y":
                    main()
                elif answer == "n" or answer == "N":
                    exit()

        # If a guess is incorrect, the guessesLeft variable decreases as a
        # visible indiactor of the "hanging man" is shown to the user.
        elif str(inputLetter) not in word:
            print("That letter does not appear in the word! Try again!")
            guessesLeft -= 1
            print(wordProgress)
            if guessesLeft == 6:
                hangmanGallows()

            elif guessesLeft == 5:
                hangmanGallows2()

            elif guessesLeft == 4:
                hangmanHead()

            elif guessesLeft == 3:
                hangmanArmLeft()

            elif guessesLeft == 2:
                hangmanArmRight()

            elif guessesLeft == 1:
                hangmanLegLeft()

            elif guessesLeft == 0:
                hangmanLegRight(word)
            print(wordProgress)
        else:
            print("Invalid input")

def retry():
    main()

def hangmanGallows():
    print("_________")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("")
    print("You have 6 guesses left!")

def hangmanGallows2():
    print("_________")
    print("|      |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("")
    print("You have 5 guesses left!")

def hangmanHead():
    print("_________")
    print("|      |")
    print("|      O")
    print("|")
    print("|")
    print("|")
    print("|")
    print("")
    print("You have 4 guesses left!")

def hangmanArmLeft():
    print("_________")
    print("|      |")
    print("|      O")
    print("|     /|")
    print("|")
    print("|")
    print("|")
    print("")
    print("You have 3 guesses left!")

def hangmanArmRight():
    print("_________")
    print("|      |")
    print("|      O")
    print("|     /|\\")
    print("|")
    print("|")
    print("|")
    print("")
    print("You have 2 guesses left!")

def hangmanLegLeft():
    print("_________")
    print("|      |")
    print("|      O")
    print("|     /|\\")
    print("|     / ")
    print("|")
    print("|")
    print("")
    print("You have 1 guesses left!")

def hangmanLegRight(word):
    print("_________")
    print("|      |")
    print("|      O")
    print("|     /|\\")
    print("|     / \\")
    print("|")
    print("|")
    print("")
    print("You are out of guesses you lose! Oof.")
    print("The word was "+word)
    print("")
    answer = input("Would you like to play again? (Y/N)")
    if answer == "y" or answer == "Y":
        main()
    elif answer == "n" or answer == "N":
        exit()


main()
