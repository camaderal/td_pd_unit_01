"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

MIN_NUM = 1
MAX_NUM = 10

def start_new_session():
    num_attempts = 0;
    number_to_guess = random.randint(MIN_NUM, MAX_NUM)

    print("============================")
    print("Start!")
    while True:
        guess = input("Input a number from {}-{}: ".format(MIN_NUM, MAX_NUM))
        try:
            guess = int(guess)
            if guess < MIN_NUM or guess > MAX_NUM:
                raise ValueError("Number must be between {}-{}".format(MIN_NUM, MAX_NUM))
        except ValueError as err: 
            print("Invalid input({}). Please try again.".format(err))
            continue

        num_attempts+=1
        if guess > number_to_guess:
            print("It's lower")
        elif guess < number_to_guess:
            print("It's higher")
        else:
            print("You got it! It took you {} attempts.".format(num_attempts))
            print("============================")
            return num_attempts

def start_game():
    high_score = 0

    print("============================")    
    print("||   Guess The Number     ||")
    print("============================")
    print("")
    name = input("What is your name? ")
    print("Welcome, {}! ".format(name))

    while True:
        print("")
        if high_score:
            print("--Current High Score is {}--".format(high_score))
        else:
            print("--No High Score Set--")
        print("============================")
        print("[N] New Game.")
        print("[E] Exit.")
        print("============================")
        print("")

        choice = input("> ")
        if choice.upper() == "N":
            score = start_new_session()
            if not high_score or high_score > score:
                print("Congratulations! You beat the high score!")
                high_score = score
        elif choice.upper() == "E":
            break
        else:
            print("Invalid Input. Please Try Again.")

start_game()