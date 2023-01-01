shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None   # used as a constant to show variable doesn't have a value (similar to NULL in java)

for index in range(len(shopping_list)):     # len() shows how many values in sequence
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("Item found at position {}".format(found_at))
