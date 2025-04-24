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
            print(computer_choice)
            os.system("pause & cls")
        elif computer_choice == 2:
            print("Computer Wins")
            computer_score += 1
            computer_choice = "Paper"
            print(computer_choice)
            os.system("pause & cls")
        else:
            print("Player Wins")
            player_score += 1
            computer_choice = "Scissor"
            os.system("pause & cls")
    elif player_choice.title() == "Paper":
        if computer_choice == 1:
            print("Player Wins")
            computer_choice = "Rock"
            print(computer_choice)
            os.system("pause & cls")
        elif computer_choice == 2:
            print("Draw")
            computer_score += 1
            computer_choice = "Paper"
            print(computer_choice)
            os.system("pause & cls")
        else:
            print("Computer Wins")
            player_score += 1
            computer_choice = "Scissor"
            os.system("pause & cls")
    elif player_choice.title() == "Scissor":
        if computer_choice == 1:
            print("Computer Wins")
            computer_choice = "Rock"
            print(computer_choice)
            os.system("pause & cls")
        elif computer_choice == 2:
            print("Player Wins")
            computer_score += 1
            computer_choice = "Paper"
            print(computer_choice)
            os.system("pause & cls")
        else:
            print("Draw")
            computer_choice = "Scissor"
            os.system("pause & cls")
    else:
        print("Stupid")
