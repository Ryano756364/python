day = "Monday"
tempurate = 30
raining = True  # capital T

# watch order precedence with 'and' and 'or' and use () to notate goal of expression
# and has higher precedence than or
if day == "Saturday" and tempurate > 27 or not raining:    # notice the == and NOT .equals() in Java
    print("Go swimming")
else:
    print("Learn Python")
