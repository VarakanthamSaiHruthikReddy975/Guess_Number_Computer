import random #We import the random number generator package

def guess_number(number):
    random_number = random.randint(1,number)
    guess = 0
    #until the user enters the right number this while loop continues until the computer's random number matches the user entered number
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {number} "))
        if guess < random_number:
            print("Try again.... too low")
        elif guess > random_number:
            print("Try again..... too high")

    print(f"You are spot on .... you got it right {random_number}") #Once the guess equals random number we print that the user had found the number
guess_number(10)