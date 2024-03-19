""" 
Guessing Game

I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

- Prompts the user for a level, N If the user does not input a positive integer, 
the program should prompt again.
- Randomly generates an integer between 1 and, inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, 
the program should prompt the user again.
    - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    - If the guess is the same as that integer, the program should output Just right! and exit.

"""
import random
import sys

def main():
    game()


def game():
    while True:
        try:
            level = int(input("Level: "))
            num = random.randint(1, level)

            while True:
                try:
                    guess = int(input("Guess: "))

                    if guess > num:
                        print("Too large!")
                    elif guess < num:
                        print("Too small!")
                    elif guess == num:
                        sys.exit("Just right!")

                except (ValueError, TypeError):
                    pass
        except (ValueError, TypeError):
            pass


if __name__ == "__main__":
    main()