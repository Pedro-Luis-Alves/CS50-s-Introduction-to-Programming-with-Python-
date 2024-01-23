"""
Einstein
Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc^2, where:

'E' represents energy (measured in Joules)
'm' represents mass (measured in kilograms)
'c'represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al.

Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) 
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""
#----------------------------------------

m = int(input("Please, insert the number for m"))
c = 300000000
E = m*c*c
print(E)