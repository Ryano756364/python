shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatross"  # will end up "Item found at None"
found_at = None   # used as a constant to show variable doesn't have a value (similar to NULL in java)

# better way to write this
# for index in range(len(shopping_list)):     # len() shows how many values in sequence
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# the better way to write this
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
# this can still be more efficient

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
