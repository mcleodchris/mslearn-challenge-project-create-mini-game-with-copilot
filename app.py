# prompt the user for one of 3 options: rock, paper, or scissors. Warn the user if they enter an invalid option.
# generate a random computer choice
# compare the user's choice and the computer's choice
# determine the winner through the following means:
# rock beats scissors
# scissors beats paper
# paper beats rock
# inform the user who the winner is
# ask the user if they want to play again
# if the user says yes, restart the game
# if the user says no, exit the game
# if the user enters an invalid option, ask them again
# if the user enters an invalid option 3 times, exit the game

import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()

def play_game():
    user_choice = input("Please choose rock, paper, or scissors: ").lower()
    #warn the user if they enter an invalid option
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        play_game()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
        scores["tie"] += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        scores["user"] += 1
    else:
        print("You lose!")
        scores["computer"] += 1

    play_again()

def play_again():
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    elif play_again == "no":
        print("Thanks for playing!")
        print(f"Scores: User - {scores['user']}, Computer - {scores['computer']}, Tie - {scores['tie']}")
    else:
        print("Invalid choice. Please try again.")
        play_again()

scores = {"user": 0, "computer": 0, "tie": 0}

if __name__ == "__main__":
    main()

