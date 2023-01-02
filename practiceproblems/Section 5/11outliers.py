data = [4, 5, 104, 105, 110, 120, 160, 260, 275]

# del data[0:2]
print(data)  # [104, 105, 110, 120, 160]

# or

min_valid = 100
max_valid = 200

# this will not work
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)  # [104, 105, 110, 120, 160, 275]

# why is 275 there?
# the loop already removed second to last position and 275 moved into 260's position


# process the low values in the list, list must be ordered
# no new list was created here
stop = 0;
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)


# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):  # second -1 makes us start at the end
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # set 'start' to teh position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break
print(start)  # for debugging
del data[start:]
print(data)