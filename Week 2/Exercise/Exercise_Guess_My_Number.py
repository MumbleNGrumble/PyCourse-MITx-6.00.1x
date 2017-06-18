# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:42:31 2017

@author: Daniel
"""

print("Please think of a number between 0 and 100!")
startRange = 0
endRange = 100

while True:
    guess = (startRange + endRange)//2
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if response == "h":
        endRange = guess
    elif response == "l":
        startRange = guess
    elif response == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")