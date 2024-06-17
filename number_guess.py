import random as r
import math as m

def game_start():

    count = 10

    npc_guess = r.randint(1,100)

    game_loop(npc_guess, count)

def game_loop(npc_guess, count):

    while (count > 0):

        user_guess = int(input("What is your guess between 1-100?\n"))

        if user_guess == npc_guess:
            print(f"Nice! You've got it! The number is {npc_guess}!")
            print(f"Congrats! You've got it with {count} tries left!\n")
            break
        elif user_guess > npc_guess:
            print("Your guess is too high! Please try again!")
            count = count - 1            
            print(f"You've {count} tries left.\n")
        elif user_guess < npc_guess:
            print("Your guess is too low! Please try again!")
            count = count - 1
            print(f"You've {count} tries left.\n")
        else:
            print("That's not a valid guess buddy. Try again!\n")
            count = count - 1

    if count == 0:
        print(f"The random number was actually {npc_guess}! That's too bad :(")

def main():
    response = (input("Do you wish to play the number guessing game? 'yes/no'\n",))

    if response == "yes":
        print("Alrighty! Let's play!\n")
        game_start()

    elif response == "no":
        print("Okay, bye then!\n")

main()
