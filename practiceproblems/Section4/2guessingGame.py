answer = 5

print("Please guess number between 1 and 10: ")
# converts all their input to an int
guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:    # could've use a second if here
    print("Please guess lower")
else:   # if number is 5, else does not get evaluated, it goes striaght into the suite
    print("You got it first time")

# this video showed intro steps to debugging
