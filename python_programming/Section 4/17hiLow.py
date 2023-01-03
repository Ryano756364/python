low = 1
high = 1000

print("Please think of a number between {} and {} ".format(low, high))
input("Press enter to start ")

guesses = 1

# user picks a number on their own then computer tries to figure out that number in under 10 guesses
# want computer to stop once right answer is found
while True:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2     # integer division
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter 'h', 'l', or 'c'. \n"
                     .format(guess).casefold())

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1

    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break

    else:
        print("Please enter h, l, or c")

    # Make sure to use augmented assigned as guesses = guess + 1 is less efficient
    # in Java it wouldn't be as efficient because  Python evaluates guesses twice
    # AA also works on strings too
    guesses += 1

# binary search | integer division | pass
# Python doesn't have Case or Switch Statements
