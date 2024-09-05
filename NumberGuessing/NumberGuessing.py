from random import randint
from art import logo

easy_mode = 10
hard_mode = 5

def select_mode():
    selection = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if selection == "easy":
        return easy_mode
    elif selection == "hard":
        return hard_mode
    else:
        return 0

def checker(user_guess, computer_choice,turns):
    if user_guess > computer_choice:
        if (user_guess - computer_choice) > 10:
            print("Too High!")
            return turns - 1
        elif (user_guess - computer_choice) > 5:
            print("A bit High!")
            return turns - 1
        else:
            print("Still high, but you are very close!")
            return turns - 1
    elif user_guess < computer_choice:
        if (computer_choice - user_guess) > 10:
            print("Too Low!")
            return turns - 1
        elif (computer_choice - user_guess) > 5:
            print("A bit Low!")
            return turns - 1
        else:
            print("Still low, but you are very close!")
            return turns - 1
    else:
        print(f"You got it! The answer was {computer_choice}")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_choice = randint(1, 100)
    print(computer_choice)

    turns = select_mode()
    game_status = True
    while game_status:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns = checker(user_guess, computer_choice,turns)
        if user_guess == computer_choice:
            return
        if turns == 0:
            print("You've run out of guesses, you lose.")
            game_status = False
        elif user_guess != computer_choice:
            print("Guess again.")

game()