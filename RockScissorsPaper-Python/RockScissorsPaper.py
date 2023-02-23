import random
choices = ["rock","scissors","paper"]

computer=random.choice(choices)
player=None
while player not in choices:
    player = input("rock ,scissors ,paper : ").lower()

if(computer==player):
    print("computer :"+computer)
    print("player : "+player)
    print("It is tie!")
elif(player=="rock"):
    if computer=="paper":
        print("computer :" + computer)
        print("player : " + player)
        print("Computer wins!")
    elif computer=="scissors":
        print("computer :" + computer)
        print("player : " + player)
        print("Player wins!")
elif(player=="paper"):
    if computer=="scissors":
        print("computer :" + computer)
        print("player : " + player)
        print("Computer wins!")
    elif computer=="rock":
        print("computer :" + computer)
        print("player : " + player)
        print("Player wins!")
elif(player=="scissors"):
    if computer=="rock":
        print("computer :" + computer)
        print("player : " + player)
        print("Computer wins!")
    elif computer=="paper":
        print("computer :" + computer)
        print("player : " + player)
        print("Player wins!")


