import os
import random

game_Loop = True
player_score = 0
computer_score = 0

while game_Loop:
    print(f"Rock Paper Scissor\nPlayer Score: {player_score}\nComputer Score: {computer_score}")
    player_choice = input("Choose Rock, Paper, Scissor: ")
    computer_choice = random.randint(1, 3)
    if player_choice.title() == "Rock":
        if computer_choice == 1:
            print("Draw")
            computer_choice = "Rock"
        elif computer_choice == 2:
            print("Computer Wins")
            computer_score += 1
            computer_choice = "Paper"
        else:
            print("Player Wins")
            player_score += 1
            computer_choice = "Scissor"
        print(f"Computer Chose {computer_choice}")
        Enter = True
    elif player_choice.title() == "Paper":
        if computer_choice == 1:
            print("Player Wins")
            player_score += 1
            computer_choice = "Rock"
        elif computer_choice == 2:
            print("Draw")
            computer_choice = "Paper"
        else:
            print("Computer Wins")
            computer_score += 1
            computer_choice = "Scissor"
        print(f"Computer Chose {computer_choice}")
        Enter = True
    elif player_choice.title() == "Scissor":
        if computer_choice == 1:
            print("Computer Wins")
            computer_score += 1
            computer_choice = "Rock"
        elif computer_choice == 2:
            print("Player Wins")
            player_score += 1
            computer_choice = "Paper"
        else:
            print("Draw")
            computer_choice = "Scissor"
        print(f"Computer Chose {computer_choice}")
        Enter = True
    else:
        print("Invalid Input. Please try again.")
        Enter = False
        os.system("pause & cls")

    while Enter:
        Input = input("Enter Q to Quit, R to Restart or Press Enter to Continue:").upper()
        if Input == "Q":
            game_Loop = False
            Enter = False
        elif Input == "R":
            Enter = False
            player_score = 0
            computer_score = 0
            os.system("cls")
        else:
            Enter = False
            os.system("cls")
