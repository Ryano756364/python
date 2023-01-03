# 0 is False
if 0:
    print("True")
else:
    print("False")

# empty strings are False
name = input("Please enter your name: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the person with no name?")


day = "Monday"
tempurate = 30
raining = True  # capital T

# watch order precedence with 'and' and 'or' and use () to notate goal of expression
# and has higher precedence than or
if day == "Saturday" and tempurate > 27 or not raining:    # notice the == and NOT .equals() in Java
    print("Go swimming")
else:
    print("Learn Python")