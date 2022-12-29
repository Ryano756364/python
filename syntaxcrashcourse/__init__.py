#!/usr/bin/env python3

# Good tutorial at https://docs.python.org/3/tutorial

name = input("What is your name? ")
print("Hello, " + name)

# Each line of code that ends with a line break is a statement or a simple statement
# A section of code that evaluates a single value is called an expression

name = "Jason"
if name != "":  # Header, all code in this block is called a suite
    message = "Hello, " + name + "!"
    print(message)
print("I am a computer")  # This will run everytime because it's not a part of suite

raining = True
if raining: pass  # Python offers pass which does absolutely nothing but can be important

""" Docstrings are seen by the interpreter; comments are ignored """
""" Docstrings are used in automatic documentation generation """
""" Docstrings are only docstrings when they appear at top of module, function, class or method they define """
#Try to avoid using them for multi line comments

#Variables
#Python is dynamically typed meaning the type of value is determined when it is evaluated
#i.e. string versus int
#Don't change values throughout program
#Python is a 'strongly typed language' meaning you usually can't magically combine data of different types
#JavaScript is weakly typed
#Python is 'weakly bound' meaning it is possible to assign a value of a different type to a variable

#Constants
#There is a direct way to assign constants but use SCREAMING_SNAKE_CASE when you do
#You are still capable of chaning the variable, but the linter will complain if you do in keeping with PEP 8

