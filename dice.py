
#ver_2.0
import random
min = 1
max = 6

while True:
    answer = input("Do you want to play dice (yes or no): ")

    if answer == "yes":
        print("Rolling the dices...")
        print("The values are....")
        print(random.randint(min, max))
        print(random.randint(min, max))
    elif answer == "no":
        print("OK bye bye!")
        break
    else:
        print("Please enter yes or no.")
