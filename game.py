"""A number-guessing game."""

# Put your code here
import random


name = input("Howdy, what's your name?\n(type in your name) ")
number_guessed = int(input(f"{name}, I'm thinking of a number between 1 and 100.\nTry to guess my number.\nYour guess? "))

number = random.randint(1, 101)

counter = 0
# Create function for guessing


def guess_num(number_guessed):
    while number_guessed != number:
        if number_guessed > number:
            counter += 1
            number_guessed = input('Your guess is too high, try again. \n Your guess?')
        elif  number_guessed < number:
            counter += 1
            number_guessed = input("Your guess is too low, try again. \n Your guess?")
    
    print(f"Well done,{name}. You found my number in {counter} tries.")


