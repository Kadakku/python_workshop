#need to include try except
import random

guesses_taken = 0

name = input("Hello what's your name: ")

number = random.randint(1, 99)
print("Well", name, "I'm thinking of a number between 1 and 99.")
print(number)
while guesses_taken < 6:
    guess = int(input("Take a guess:"))
    guesses_taken += 1

    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is to high")
    else:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print("Good job,", name, "You guessed my number in", guesses_taken, "guesses")
else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

