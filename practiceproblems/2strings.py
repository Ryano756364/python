# When the program is running, everything the program needs ends up stored in the computer's memory.
# The program code itself will be stored in one area of memory, and the data works on will also be stored in memory

# Variable is just a way to give a name to an area of memory

print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')

# we can concatenate too
print("hello" + " world")

# greeting is the 'name'
# Hello is the 'value'
# Whenever we use greeting, Python knows we are talking about Hello
# greeting is BOUND to hello
greeting = "Hello"
name = "Ryan"

print(greeting + " " + name)

age = 24
print(age)

print(type(greeting))  # <class 'str'>
print(type(age))  # <class 'int'>

# in Python, you can also re-bind
age = "2 years"  # no longer an int
print(age)    # 2 years
print(type(age))  # <class 'str'>

# think of variable as a NAME bound to a VARIABLE OR LABEL
# Python is NOT weakly typed
# rebinding is what happens when flipping from int to String (although you don't want to do it in real life)

