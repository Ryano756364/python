# expressions can be used in the format method
# the :(number) formats the column to have 2 and 4 placeholders to line up values, respectively
for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))

print()

# if we use the <, we can align left
# whereas above, align right is left alone
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:4}".format(i, i**2, i**3))

# or center the data with ^ as the last {} is done this way
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))


print("Pi is approx {0:12}".format(22 / 7))
print("Pi is approx {0:12f}".format(22 / 7))
print("Pi is approx {0:12.50f}".format(22 / 7))     # precision of 50 digits
