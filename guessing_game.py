import random

def start_game():
    secret_number = random.randint(1,100)
    attempts =0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts +=1

            if guess < secret_number:
                print("Too low! Try again.\n")
            elif guess > secret_number:
                print("Too high! Try again.\n")
            else:print(f"congratulation! You guessed it in{attempts} attempts!")
            break
        except ValueError:
            print("please enter a valid whole number!\n")

start_game()
        