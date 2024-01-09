# ROCK, PAPER, AND SCISSORS GAME 
import random

options = ("ROCK","PAPER","SCISSORS")
play = True

while play:
    YOU = None
    AI_BOT = random.choice(options)

    while YOU not in options:
        YOU = input("\n\nEnter the choice(ROCK , PAPER , SCISSORS) : ").upper() 
        
        print(f"YOU: {YOU}")
        print(f"AI_BOT: {AI_BOT}")

        if YOU == AI_BOT:
            print("It's a tie...\n")
        elif YOU == "ROCK" and AI_BOT == "SCISSORS":
            print("You Win!\n")
        elif YOU == "SCISSORS" and AI_BOT == "PAPER":
            print("You Win!\n")
        elif YOU == "PAPER" and AI_BOT == "ROCK":
            print("You Win!\n")
        elif YOU not in options:
            print("\n\n________________________________________________\n\nRule violation!!!\nPlease select the choice from options or check for spelling \nTry Again!\n________________________________________________")
        else:
            print("YOU Lose!")

        if not input("\n________________________________________________\n\nPress Y/y to play again\nElse Press any key to exit : ").lower()  == "y":
            play = False
print("\nThanks for playing!\n")