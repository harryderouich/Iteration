#Harry Derouich
#11/11/14
#Iteration Spot Check - Question 3

import random

guessed = False
no_of_turns = 0

number = random.randint(1,101)

while guessed == False:
    no_of_turns = no_of_turns + 1
    user_guess = int(input("Please enter your guess: "))
    if user_guess == number:
        guessed = True
    elif user_guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

print("You took {0} guesses to guess the number".format(no_of_turns))
print("The number was: {0}".format(number))
