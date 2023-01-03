import random


def get_integer(prompt):  # gets input from user and returns int value
    while True:  # keep looping until value is valid
        temp = input(prompt)
        if temp.isnumeric():  # makes sure temp...is numeric
            return int(temp)
        else:
            print("Not a valid number")


highest = 1000
answer = random.randint(1, highest)
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer("-> ")  # prompt argument being sent

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")
