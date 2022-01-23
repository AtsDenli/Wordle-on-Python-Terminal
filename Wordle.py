import random
from colorama import Fore, Style


def check(guess, Dictionary):
    isIn = False
    for word in Dictionary:
        if guess == word[0:5]:
            isIn = True
    return isIn


Dictionary = []

again = "y"

with open("Dictionary_complete1.txt", "r") as file:
    for line in file:
        Dictionary.append(line)

print(
    "Welcome to Wordle! The game works exactly the same as it did, except I didn't do the design."
)

while again == "y":
    word = random.choice(Dictionary)
    guesses = 1
    solved = False
    already = []
    notIn = []

    for k in range(5):
        print(f"Guess a word ({guesses})")
        print(notIn)
        guess = input()

        while check(guess, Dictionary) != True:
            print(
                "Please enter a valid input. It must be 5 letters long and in the English Dictionary."
            )
            guess = input()

        if guess == word[0:5]:
            print(Fore.GREEN + guess, end='')
            solved = True
            print(Style.RESET_ALL)
            print("Well done!")
            break

        already = []

        for j in range(5):
            if solved == True:
                break
            elif guess[j] == word[j]:
                print(Fore.GREEN + guess[j], end='')
                print(Style.RESET_ALL, end='')
            elif guess[j] in word and not guess[j] in already:
                print(Fore.YELLOW + guess[j], end='')
                print(Style.RESET_ALL, end='')
                already.append(guess[j])
            else:
                print(guess[j], end='')
                if not guess[j] in notIn:
                    notIn.append(guess[j])

        print()
        guesses += 1

    print(word)

    print("Would you like to go again? y/n")
    again = input()
