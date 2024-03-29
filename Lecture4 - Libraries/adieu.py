""" 
Adieu, Adieu

In The Sound of Music, there’s a song sung largely in English, 'So Long, Farewell', 
with these lyrics, wherein “adieu” means “goodbye” in French:

| "Adieu, adieu, to yieu and yieu and yieu"

Of course, the line isn’t grammatically correct, since it would typically 
be written (with an Oxford comma) as:

| "Adieu, adieu, to yieu, yieu, and yieu"

To be fair, “yieu” isn’t even a word; it just rhymes with "you"!

In a file called adieu.py, implement a program that prompts the user for names, 
one per line, until the user inputs control-d. Assume that the user will input 
at least one name. Then bid adieu to those names, separating two names with one 
'and', three names with two commas and one 'and', and N names with N-1 commas and one 'and':

"""
import inflect

def main():
    adieu()


def adieu():
    flex = inflect.engine()
    names = []

    while True:
        try:
            names.append((input("Name: ").title()))
        
        except EOFError:
            return print("Adieu, adieu, to", flex.join(names))


if __name__ == "__main__":
    main()