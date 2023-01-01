number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)   # prints ->    ,;: ,;

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))  # prints [9, 223, 372, 36, 854, 775, 807]

# check built-ing functions in python documentation
