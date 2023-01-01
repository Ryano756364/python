available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")

print("Aren't you glad you got out of there? ")

# while loops are good when you don't know how many loops
# or for reading data from file or an internet stream
# good for file input and output
