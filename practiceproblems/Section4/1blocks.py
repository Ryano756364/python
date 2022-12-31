for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("Please enter your name: ")
# when you want to get number from user
# could cause serious problem if anything but number is entered
# will talk about how to fix later in course
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# can be flipped
# start with more limiting to more broad
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")