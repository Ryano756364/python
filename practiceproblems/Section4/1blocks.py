for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("Please enter your name: ")
# when you want to get number from user
# could cause serious problem if anything but number is entered
# will talk about how to fix later in course
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    # both of these run because they are in the same code blocks
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
else:
    print("You are old enough to vote")
    print("Please put an X in the box")