# careful here because a file name of 'range' could cause issues

# second value is not included
for i in range(1, 20):  # usually you want to avoid single case variables except in loops
    print("i is now {}".format(i))


for i in range(1, 21):  # here's how we include 20
    print("i is now {}".format(i))