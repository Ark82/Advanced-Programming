import random


Random_Number = random.randint(1, 100)
print(f"Random_Number is: {Random_Number}")
print("""Hello, welcome to the number guessing game.
In order to win in this game you have to guess the randomly generated number between 1 to 100.
The amount of tries that takes you to finish this game will be accounted for so be mindful.""")
Guess = int(input("Enter your first guess: "))
Numbers_Guessed = []
Amount_Of_Tries = 0
while True:
    if Guess == Random_Number:
        print(f"You have won the guessing game!!!\nIt took you {Amount_Of_Tries} tries to beat this game")
        break
    else:
        if Numbers_Guessed.count(Guess):
            print("You have tried this number before!\nGuess again: ", end="")
        else:
            Amount_Of_Tries += 1
            Numbers_Guessed.append(Guess)
            print("Wrong number,Guess again: ", end="")
        Guess = int(input())
