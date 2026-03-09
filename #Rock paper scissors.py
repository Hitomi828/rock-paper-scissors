#Rock paper scissors


#Homework Week 6
#Write a program that allows users to play a game of paper, scissors, rock with the computer.
#Your program needs to have:
#• At least one CONSTANT
#• At least two functions
#• Be well-commented
#• Have at least one loop (For, While True)
#• Must allow the user to decide to either or not they want to ‘see’the instructions for how to play. 
#• Should not crash if users put in invalid answers.
#• During the game, users should be able to type either the full word (rock / paper / scissors) or the first letter of the word (R / P / S) to indicate their choice.
#• Remember that…
#• Paper beats rock
#• Rock beats scissors
#• Scissors beats paper
#• Users after each round should be able to either A) Leave or B) Continue playing.
#You will need to provide evidence of:
#• Testing user input: invalid and valid
#• Debugging (even if you have no bugs you will need evidence of this).
#You will:
#• Submit your working code + any other versions to Schoology (I highly recommend that you are submitting your code to GitHub – if you are doing this please just submit your GitHub file)
#• Your evidence.
#This is due on Monday

#Virsion 4

import random
import string

#CONSTANTS =　定数
#list of all valid choices the game can use

CHOICES = ["rock","paper","scissors"]

#Welcome text
def welcome_text():
    print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█

█▀█ █▀█ █▀▀ █▄▀ ▄▄ █▀█ ▄▀█ █▀█ █▀▀ █▀█ ▄▄ █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀ █ █ █ █
█▀▄ █▄█ █▄▄ █░█ ░░ █▀▀ █▀█ █▀▀ ██▄ █▀▄ ░░ ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█ ▄ ▄ ▄ ▄""")
    

#Clean input
def cleaned_input(user_input: str) -> str:
    cleaned = user_input.lower()
    cleaned = cleaned.replace(" ","")
    cleaned = cleaned.strip(string.punctuation)
    return cleaned

#Instructions

#Print the instructions for how to play the game.

def show_instructions(): #関数
    print("""
How to play Rock-Paper-Scissors:
-Rock beats Scissors 
-Scissors beats Paper 
-Paper beats Rock 
Type 'rock','paper',or'scissors'. 
You can also type 'r','p','s'
""")


#Asks the user if they want to see the instructions.

def ask_show_instructions():
    while True: #無効なものでもクラッシュしないように
        answer = input("Do you want to see the instructions? yes/no " ).lower().strip() #文字の大小の自由
        answer = cleaned_input(answer)

        if answer in ["yes","y"]:
            show_instructions()
            return
        elif answer in ["no","n"]:
            return
        else:
            print("Please answer yes or no.") #Ask again

#Ask if ready to play

def ready_to_play():
    while True:
        ready = input("Ready to play???? yes/no ")
        ready = cleaned_input(ready)

        if ready in ["y","yes"]:
            print("Great! lets start!!!")
            return True
        elif ready in ["n","no"]:
            print("Come back leter...bye")
            return False
        else:
            print("invalid answer. Please type yes or no")
  

#User choice
#Gets the user choice and keep asking until its valid

def get_user_choice():
    while True:
        choice = input("Rock, Paper, Scissors? (r/p/s):").lower().strip()
        choice = cleaned_input(choice)

        #Convert short inputs to full words
    
        if choice in ["r","rock"]:
            return "rock"
        elif choice in ["p","paper"]:
            return "paper"
        elif choice in ["s","scissors"]:
            return "scissors"
        else:
            print("Invaild choice. Please type rock/paper/scissors or r/p/s.")


#Computer choice
#Randomly selects rock,paper,or scissors for the computer
def get_computer_choice():
    return random.choice(CHOICES)


#Decide winner

def decide_winner(user,computer):
    if user == computer:
        return "draw"
    if (user == "rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):
        return "win" #all winning conditions for the user
    else:
        return "lose" #not win or draw, user lose


#play one round　一回分のじゃんけんの関数

def play_round():
    user = get_user_choice()
    computer = get_computer_choice()

    print(f"You choice: {user}")
    print(f"Computer chose: {computer}")

    result = decide_winner(user, computer) #Determine the winner

    #print the result
    if result == "win":
        print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗  ██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║  ██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║  ██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║  ╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║  ██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝""")
    elif result == "lose":
        print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗░░░░░░░░░░░░░░░
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝░░░░░░░░░░░░░░░
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░░░░░░░░░░░░░░░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░░░░░░░░░░░░░░░░
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗██╗██╗██╗██╗██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝╚═╝╚═╝╚═╝╚═╝""")
    else:
        print("""
██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║  ██║
██║░░██║██████╔╝███████║░╚██╗████╗██╔╝  ██║
██║░░██║██╔══██╗██╔══██║░░████╔═████║░  ╚═╝
██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░  ██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░  ╚═╝""")


#Main game loop

def main():
    welcome_text()
    ask_show_instructions()

    while True:
        if ready_to_play():
            play_round()
        else:
            break

        again = input("Do you want to play again??? yes/no ").lower().strip()
        again = cleaned_input(again)

        if again not in ["yes","y"]: #if doesnt say yes, end the game
            print("""
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █▀█ █░░ ▄▀█ █▄█ █ █▄░█ █▀▀   █
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▀▀ █▄▄ █▀█ ░█░ █ █░▀█ █▄█   ▄""")
            break

#start te game
main() #main()は必須