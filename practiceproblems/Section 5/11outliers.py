data = [4, 5, 104, 105, 110, 120, 160, 260, 275]

del data[0:2]
print(data)  # [104, 105, 110, 120, 160]

# or

min_valid = 100
max_valid = 200

# this will not work
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]

print(data)  # [104, 105, 110, 120, 160, 275]

# why is 275 there?
# the loop already removed second to last position and 275 moved into 260's position
