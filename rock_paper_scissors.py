import random

computer_plays = ["Rock", "Paper", "Scissors"]

user_play = ""
computer_play = ""

print("Plays: \n Rock = R \n Paper = P \n Scissors = S")
print('Type "end" to end game')

def rock():
    if computer_play == "Rock":
        print("Tie Game!")
    elif computer_play == "Paper":
        print("You Lose!")
    elif computer_play == "Scissors":
        print("You Win!") 

def paper():
    if computer_play == "Rock":
        print("You Win!")
    elif computer_play == "Paper":
        print("Tie Game!")
    elif computer_play == "Scissors":
        print("You Lose!")

def scissors(): 
    if computer_play == "Rock":
        print("You Lose!")
    elif computer_play == "Paper":
        print("You Win!")
    elif computer_play == "Scissors":
        print("Tie Game!")

while True:

    user_play = input("Choose Play: ").upper()
    computer_play = random.choice(computer_plays)

    if user_play == "R":
        print("Computer Chose: " + computer_play)
        rock()
    elif user_play == "P":
        print("Computer Chose: " + computer_play)
        paper()
    elif user_play == "S":
        print("Computer Chose: " + computer_play)
        scissors()
    elif user_play == "end":
        print("Thanks for playing!")
        break
