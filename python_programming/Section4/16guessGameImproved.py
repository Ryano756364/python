# random comes from a module called 'random'
# import allows us to use all the objects from that module
import random

highest = 10
answer = random.randint(1, highest)
quitGame = False

print("Guess number between 1 and {}: (type '0' to exit the program) ".format(highest))

# use while loop to allow player to keep guessing
while not quitGame:
    guess = int(input())

    if guess == 0:
        break;
    elif guess == answer:
        print("You got it! ")
        break
    elif guess < answer:
        print("Please guess higher (or q) ")
    else:
        print("Please guess lower (or q) ")

# generate random number
