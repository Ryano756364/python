# careful here because a file name of 'range' could cause issues

# second value is not included
for i in range(1, 20):  # usually you want to avoid single case variables except in loops
    print("i is now {}".format(i))


for i in range(1, 21):  # here's how we include 20
    print("i is now {}".format(i))

for i in range(21):  # default value is 0 if no start value is included
    print("i is now {}".format(i))

# step value
for i in range(0, 10, 2):  # steps 2
    print("i is now {}".format(i))
# prints
# i is now 0
# i is now 2
# i is now 4
# i is now 6
# i is now 8

# count backwards
for i in range(10, 0, -2):  # steps 2
    print("i is now {}".format(i))
# prints
# i is now 10
# i is now 8
# i is now 6
# i is now 4
# i is now 2
