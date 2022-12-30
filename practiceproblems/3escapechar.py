splitString = "This string have been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4"
print(tabbedString)

# To use single quotes inside a string literally already created with single quote '
print('The pet shop owner said "No, no, \'e\'s uh, ...he\'s resting".')
print("""This also works too for for '' and "" inside a string literal""")

anotherSplitString = """This string has been 
split 
over
several line"""
print(anotherSplitString)  # prints exactly how it's typed out here

anotherSplitString = """This string has been \
split \
over \
one line"""
print(anotherSplitString)  # prints one line

# what if you wanted to use the \ character
print("This will add a \\ to the output")
# raw string can be used
print(r"This will also add a \ character")
