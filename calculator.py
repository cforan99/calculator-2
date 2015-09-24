"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

print "Welcome to our calculator!" 
print "You can perform the following operations on any two numbers: "
print "+, -, *, /, square, cube, pow, mod."
print "Please enter the operation followed by the two numbers (ex. pow 3 5)."

calc_input = ""

while calc_input != "q":
    calc_input = raw_input(">")
    terms = calc_input.split(" ")
    if terms[0] == "+":
        add_answer = add(int(terms[1]), int(terms[2]))
        print add_answer
