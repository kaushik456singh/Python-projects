import random

number = random.randint(1, 100)
guess = None
turns = 0

while guess != number:
    guess = int(input("Guess the number (1-100): "))
    turns += 1  

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! It took{turns} tries to guess the number ")
