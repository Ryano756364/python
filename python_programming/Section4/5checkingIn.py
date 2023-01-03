# in is used in 'sequences'

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

# string comparison are case-sensitive
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
