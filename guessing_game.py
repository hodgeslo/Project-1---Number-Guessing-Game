"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print(f"\n***         NUMBER GUESSING GAME         ***")
    print(f"*** The Number Guessing is easy and fun. Do you think that you can beat the high score? ***\n")

    random_number = random.randrange(1, 10)
    game_over = False
    number_of_attempts = 0
    high_score = 0
    show_high_score = 0

    while game_over == False:
        try:
            if show_high_score == 1:
                print(f"\nCurrent high score: {high_score}\n")

            player_guess = int(input("INITIAL Guess a number between 1 and 10: "))

            if player_guess < 1 or player_guess > 10:
                print(f"\nOops, try again! Enter a number between 1 and 10\n")
                show_high_score = 0
            elif player_guess == random_number:
                number_of_attempts += 1
                print(f"Got it! Attempts: {number_of_attempts}\n")

                while True:
                    play_again = input("Would you like to play again? (y/n)   ")
                    if play_again.lower() == "y":
                        game_over = False
                        random_number = random.randrange(1, 10)
                        if high_score == 0 or high_score == 1:
                            high_score = number_of_attempts
                        elif number_of_attempts < high_score:
                            high_score = number_of_attempts
                        elif number_of_attempts > high_score:
                            high_score
                        number_of_attempts = 0
                        show_high_score = 1
                        break
                    elif play_again.lower() == "n":
                        game_over = True
                        random_number = random.randrange(1, 10)
                        number_of_attempts = 0
                        print(f"\nGAME OVER! Thank you for playing. Have a good day!\n")
                        break
                    else:
                        print(f"Oops. Enter y or n")
                        continue
            elif player_guess < random_number:
                print(f"Wrong guess! It's higher.\n")
                number_of_attempts += 1
            elif player_guess > random_number:
                print(f"Wrong guess! It's lower.\n")
                number_of_attempts += 1
        except ValueError:
            print("\nOops. Please enter a number only\n")

# Kick off the program by calling the start_game function.
start_game()
