""" 
One of David’s first toys as a child, funny enough, was Little Professor, 
a “calculator” that would generate ten different math problems for David to solve. 
For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. 
If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. 
If David were to answer incorrectly, the toy would display EEE. And after three incorrect 
answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

- Prompts the user for a level, N. If the user does not input 1, 2, or 3, 
the program should prompt again.

- Randomly generates ten (10) math problems formatted as 'X + Y = ', wherein each of X and Y is a 
non-negative integer with N digits. No need to support operations other than addition (+).

- Prompts the user to solve each of those problems. If an answer is not correct 
(or not even a number), the program should output EEE and prompt the user again, 
allowing the user up to three tries in total for that problem. If the user has still 
not answered correctly after three tries, the program should output the correct answer.

- The program should ultimately output the user’s score: the number of correct answers out of 10.


Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) 
the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly 
generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

"""

import random


def main():
    level = get_level("Level: ")
    score = 0

    for i in range(9):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        miss = 0
        hit = False

        while miss != 3 and hit == False:

            try:
                guess = int(input(f"{x} + {y} = "))

            except ValueError:
                guess = -1

            if guess == answer:
               score += 1
               hit = True

            else:
                miss += 1
                print("EEE")
                
                if miss == 3:
                    print(f"{x} + {y} = {answer}")
    
    print("Score:", score)

        

def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))

            if level == 1 or level == 2 or level == 3:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()