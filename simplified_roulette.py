
from random import randrange
from math import ceil

# We ask the player the money he have to play
player_money = -1
while player_money < 100:
    try:
        player_money = int(input("What is your budget: "))
    except ValueError:
        print("You have to enter a number")
        player_money = -1
        continue
    if player_money < 100:
        print("You can't enter this table with less than 100$")
    else:
        print("Welcome to Roulette!")
        print("You start with a budget of", player_money, "$.")

money = player_money
continue_game = True

while continue_game:
    # while continue game we ask the player
    # to choose the number he will bet on
    number_bet = -1
    while number_bet < 0 or number_bet > 36:
        try:
            number_bet = int(input("Place your bet:  (between 0 and 36): "))
        except ValueError:
            print("You have to choose a number")
            number_bet = -1
            continue
        if number_bet < 0:
            print("You enter a negative number")
        elif number_bet > 36:
            print("The number you enter is greater than 36")
        else:
            print("You place your bet on", number_bet)

    # We ask the player how much he want to bet.
    bet = 0
    while bet <= 0 or bet > money:
        try:
            bet = int(input("How much would you like to bet: "))
        except ValueError:
            print("You didn't enter a number.")
            bet = -1
            continue
        if bet <= 0:
            print("The bet is negative or null.")
        elif bet > money:
            print("You can't bet that much you only have", money, "$")
        else:
            print("You bet", bet, "$")

    # The number bet and the bet were selected by the player
    # we spin the roulette

    winning_number = randrange(37)
    print("The games are done, nothing goes")
    print("The roulette wheel turns and stops on the number", winning_number)

    # We establish the player's gain
    if winning_number == number_bet:
        print("Congratulations you get", bet * 3, "$ !")
        money += bet * 3
    elif winning_number % 2 == number_bet % 2:  # They are the same color
        bet = ceil(bet * 0.5)
        print("You bet on the right color. You obtain", bet, "$")
        money += bet
    else:
        print("You lose your bet")
        money -= bet

    # We interrupt the game if the player is ruined
    if money == 0:
        print("You are ruined! Get out of the table.")
        continue_game = False
        break
    else:
        # We display the new sum available to the player
        print("You now have the following amount:", money, "$")


    stay = 0
    while stay != "yes" or stay != "no":
        stay = input("Would you like to continue playing (yes or no): ")
        if stay == "no":
            print("You leave the casino with:", money, "$")
            continue_game = False
            break
        elif stay == "yes":
            print("Monsieur love playing ;)")
            break
        else:
            print("Please write in full yes or no")


