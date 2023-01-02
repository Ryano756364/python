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
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)