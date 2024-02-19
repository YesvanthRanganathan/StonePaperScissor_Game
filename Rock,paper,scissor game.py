import random
print("Welcome to "+"Stone,Paper & Scissor"+" game")
while True:
    choices=["stone","paper","scissor"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("stone,paper,scissor :").lower()
        if player==computer:
            print("player :",player)
            print("computer :",computer)
            print("Both are Same! \n Tie!")
        elif player=="stone":
            if computer=="paper":
                print("player :",player)
                print("Computer: ",computer)
                print("you lose!")
            if computer=="scissor":
                print("player:",player)
                print("Computer: ",computer)
                print("you win!")
        elif player=="paper":
            if computer=="scissor":
                print("player: ",player)
                print("Computer : ",computer)
                print("You lose!")
            if computer=="stone":
                print("Player : ",player)
                print("Computer: ",computer)
                print("You win!")
        elif player=="scissor":
            if computer=="stone":
                print("player :",player)
                print("Computer : ",computer)
                print("You lose")
            if computer=="paper":
                print("Player : ",player)
                print("Computer: ",computer)
                print("You win!")
    play_again=input("You want to continue this game:(Yes or no)").lower()
    if play_again=="no":
        break
print("Thanks for Playing this game!!!!")