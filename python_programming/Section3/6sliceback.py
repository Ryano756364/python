letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[len(letters):0:-1]
print(backwards)    # edcb
# what step value will let us inclue a?

backwards = letters[len(letters)::-1]
print(backwards)    # edcba
# this will work

backwards = letters[::-1]
print(backwards)    # edcba
# this will work too

# slice the string to produce the last 8 characters, in reverse order
print(letters[len(letters)-1:len(letters)-9:-1])    # zyxwvuts

# slice the last four letters
print(letters[len(letters) - 4:])  # wxyz
print(letters[-4:])     # wxyz
