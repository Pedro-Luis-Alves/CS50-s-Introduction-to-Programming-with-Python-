""" 
When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
as by omitting vowels, much like Twitter was originally called twttr. In a file 
called twttr.py, implement a program that prompts the user for a str of text and 
then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
"""

def main():
    text = input("Input: ")
    twttr(text)

def twttr(text):
    vowels = ["A", "E", "I", "O", "U"]
    letters = []

    for letter in text:
        if letter.upper() in vowels:
            letter = letter.replace(letter, "")

        letters += letter
    
    phrase = "".join(letters)
    return print("Output:", phrase)

main()