'''
Number Guessing Game:
Write a program that generates a random number between 1 and 10. Use a while loop to allow the user to keep guessing the number until they get it right. Use an if-else condition inside the loop to give hints if the guess is too high or too low.
'''

import random

secret_number = random.randint(1, 10)

guessed_correctly = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")


while not guessed_correctly:
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low. Try again!")
    elif guess > secret_number:
        print("Too high. Try again!")
    else:
        print("Congratulations! You guessed the right number!")
        guessed_correctly = True
