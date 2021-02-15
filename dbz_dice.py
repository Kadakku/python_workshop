
def dbz_dice():
    import random


    dice_k1 = random.randrange(1,6)
    dice_k2 = random.randrange(1,6)
    dice_b1 = random.randrange(1,6)
    dice_b2 = random.randrange(1,6)

    kakarotto = dice_k1 + dice_k2
    bejita = dice_b1 + dice_b2

    if kakarotto > bejita:
        print("☆ Kakarotto wins because he obtain:", dice_k1, "with the first dice and", dice_k2, "with the second")
        print("where Bejita only obtain:", dice_b1, "with the first dice and", dice_b2, "with the second")
    elif kakarotto < bejita:
        print("Kakarotto loses because he obtain:", dice_k1, "with the first dice and", dice_k2, "with the second")
        print("where ☆ Bejita obtain:", dice_b1, "with the first dice and", dice_b2, "with the second")
    else:
        print("It's a tie")


while True:
    answer = input("Do you want to play DragonBall Z (y/n): ")

    if answer == "y":
        dbz_dice()
    elif answer == "n":
        print("OK bye bye!")
        break
    else:
        print("Please enter y/n.")
