#Python guessing game
import random

# generate random number
number = random.randint(1, 10)

# ask for user name
user_name = input("Hello! Please type your name: ")

# ask for user number
user_number = input("Guess a number from 1 to 10. You have five chances to get the number right: ")


# verify if user number is correct
if(user_number == number):
    print("Its correct!")
