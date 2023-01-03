available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: (or 'quit' to quit) ")
    if chosen_exit.casefold() == "quit":    # converts chosen_exit to lowercase
        print("Game over")
        break

print("Aren't you glad you got out of there? ")

# while loops are good when you don't know how many loops
# or for reading data from file or an internet stream
# good for file input and output

# break | converting text to lowercase
