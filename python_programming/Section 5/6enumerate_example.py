# variable names don't matter
# enumerate is very usefully when you need the index
for t in enumerate("abcdefgh"):
    index, character = t
    print(t)
    print(index, character)

# t prints 8 tuples
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')
# (7, 'h')

# index, character prints
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g
# 7 h

index, character = (0, "a")
print(index, character)  # 0, a

# example
recipes = [ ("Banana Bread", "Bananas", "Bread", 2022),
            ("Toast", "Butter", "Bread", 2023),
            ("Cookies", "Dough", "Chocolate Chips", 2023),
]

# solution #1
for recipe in recipes:
    recipe_name, ingredient_one, ingredient_two, date_added = recipe
    print("Recipe: {}, Ingredient #1: {}, Ingredient #2: {}, Date Added: {}"
          .format(recipe_name, ingredient_one, ingredient_two, date_added))

# or another solution more efficient, solution #2
for recipe_name, ingredient_one, ingredient_two, date_added in recipes:
    print("Recipe: {}, Ingredient #1: {}, Ingredient #2: {}, Date Added: {}"
          .format(recipe_name, ingredient_one, ingredient_two, date_added))
