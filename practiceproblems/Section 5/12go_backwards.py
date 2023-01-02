# backwards can be a safer strategy with mutable objects

data = [104, 101, 4, 105, 308, 5, 107, 100, 304, 203, 1, 304, 108]
min_valid = 100
max_valid = 200

# middle -1 is to capture first item in list
# third -1 is to operate backwards

# for index in range(len(data) -1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         del data[index]
#         print(index, data)

for index, value in enumerate(reversed(data)):
    print(index, value)  # reverse order of list
print(data)  # data in same order as it was instantiated
