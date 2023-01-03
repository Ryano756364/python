recipe_book = [
    ("Chocolate Chip Cookies", "100 Calories", 2022,
     [
         (2, "Bags of chocolate chips"),
         (2, "Tubs of dough"),
         (3, "Cans of Oil"),
         (17, "Cups of Sugar")
     ]
     ),
    ("Butter Toast", "1000 Calories", 2023,
     [
         (2, "Slices of Toast"),
         (4, "Sticks of Butter"),
         (1, "Tablespoon of Oil"),
         (4, "Bags of Chocolate Chips")
     ]
    )
]

print(recipe_book)  # [('Chocolate Chip Cookies', '100 Calories', 2022,
# [(2, 'Bags of chocolate chips'), (2, 'Tubs of dough'), ect....

print()

print(recipe_book[1][3][3])  # (4, 'Bags of Chocolate Chips')
