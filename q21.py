#21. Write a Python program to implement a number guessing game in which the user repeatedly enters guesses until the correct number is found. Display whether each guess is too high or too low. 

import random
secret_num = random.randint(1,100)
guess = 0

while guess!= secret_num:
    guess = int(input("Enter your Guess Number: "))

    if guess > secret_num:
        print("Guess no. is Too high than Secret")
    elif guess < secret_num:
        print("Guess no. is Too low than Secret")
    else:
        print("Congratulations!! Guess number is Found")