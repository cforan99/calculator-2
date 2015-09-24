"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

print "Welcome to our calculator!" 
print "You can perform the following operations on any two whole numbers: "
print "+, -, *, /, square, cube, pow, mod."
print "Please enter the operation followed by the two numbers (ex. pow 3 5)."
print "Press q to quit."

calc_input = ""

while calc_input != "q":
    calc_input = raw_input(">")
    terms = calc_input.split(" ")

    if len(terms) < 2:
        print "Oops, that didn't work. Did you forget to type something?"
    if len(terms) == 2:
        terms.append(0)
    if len(terms) >= 2:
        if terms[0] == "+":
            add_answer = add(int(terms[1]), int(terms[2]))
            print add_answer
        elif terms[0] == "-":
            subtract_answer = subtract(int(terms[1]), int(terms[2]))
            print subtract_answer
        elif terms[0] == "*":
            multiply_answer = multiply(int(terms[1]), int(terms[2]))
            print multiply_answer
        elif terms[0] == "/":
            divide_answer = divide(float(terms[1]), float(terms[2]))
            print divide_answer
        elif terms[0] == "square":
            square_answer = square(int(terms[1]))
            print square_answer
        elif terms[0] == "cube":
            cube_answer = cube(int(terms[1]))
            print cube_answer
        elif terms[0] == "pow":
            pow_answer = power(int(terms[1]), int(terms[2]))
            print pow_answer 
        elif terms[0] == "mod":
            mod_answer = mod(int(terms[1]), int(terms[2]))
            print mod_answer 
        else:
            print "Please enter an valid operation first."  