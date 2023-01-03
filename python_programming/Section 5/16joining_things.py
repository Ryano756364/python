menu = [["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "spam", "egg", "spam", "toast", "spam"]
]


# process the menu above with 6 meals that don't contain "spam"
# my solution
# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(", ".join(meal))

shopping_list = [
    "sugar",
    "eggs",
    "flour",
    "butter",
]

separator = " | "
output = separator.join(shopping_list)
print(output)

separator = ", "
output = separator.join(shopping_list)
print(output)

# items in iterable must be String -> join cannot work on integers
# lists are homogenous...typically
