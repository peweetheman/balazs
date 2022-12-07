import random

selected_number = random.randrange(1,100)
while True:
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    if guess == selected_number:
        print("You won")
        break
    elif guess < selected_number:
        print("Guess higher!")
    elif guess > selected_number:
        print("Guess lower!")
