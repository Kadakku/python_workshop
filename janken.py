from random import randint
 
print("#########################################")
print("Let's play Rock, Paper Scissors!")
print("##########################################\n\n")

startGame = input("Shall we start?(y/n)\n")

while startGame == "y":
	
    #list of play options
    playList = ["Rock", "Paper", "Scissors"]
     
    #random play to the computer
    computer = playList[randint(0,2)]
     
    #loop starts: player set to False
    player = False
     
    while player == False:
    #player set to True
        player = input("\nRock, Paper, Scissors?\n")
        if player == computer:
            print("Tie! \n")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player, "\n")
            else:
                print("You win!", player, "smashes", computer, "\n")
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player, "\n")
            else:
                print("You win!", player, "covers", computer,"\n")
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player,"\n")
            else:
                print("You win!", player, "cut", computer, "\n")
        else:
            print("That's not a valid play. Check your spelling!\n")
        #to continue loop, player set to False again
        player = False
        computer = playList[randint(0,2)]

if startGame == "n":
print("Come again later")
