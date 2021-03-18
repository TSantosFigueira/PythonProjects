#Python guessing game
import random

# generate random number
number = random.randint(1, 10)

# ask for user name
user_name = input("Hello! Please type your name: ")

# initialize the user tries count
tries = 0

# loop to make the program give the user 5 attempts
while tries < 5:

    # ask for user number
    user_number = int(input("Guess a number from 1 to 10. You have five chances to get the number right: "))
    tries += 1

    # verify if user number is correct
    if user_number == number:
        break

    elif user_number < number:
        print("Oops, too small!\n")

    elif user_number > number:
        print("Oops, too high!\n")

# Pint message to user if number os guessed or not
if user_number == number:
    print('Congratulations, you guessed the number! It only took you '
          + str(tries) + ' tries!')
else:
    print('You did not make it! The number was ' + str(number) + '.')
