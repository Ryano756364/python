age = int(input("How old are you?? "))

if 16 <= age <= 65:     # complex expression, need both to be true
    print("Have a good day at work!")
else:
    print("Enjoy your free time!")

print("-" * 80)     # simple divider

if age < 16 or age > 65:    # if first condition is hit, Python doesn't move onto second one (age > 65)
    print("Enjoy your free time!")
else:
    print("Have a good day at work!")
