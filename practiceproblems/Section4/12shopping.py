# defining list contianing 6 items, can be any object
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# continue is problem not used very often
# continue can help make code easier to read
for item in shopping_list:
    if item == "spam":
        break    # causes all remaining code in the block to be ignored; no processing happens
    print("Buy " + item)

# only prints milk, pasta, eggs
# break is good for when you are looking for items and no longer need to keep searching