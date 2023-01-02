shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list

print(id(shopping_list))  # 2195850221504
print(id(another_list))  # 2195850221504

shopping_list += ["cookies"]
print(shopping_list)  # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
print(id(shopping_list))  # 2198131660736

# lists are mutable and Python was able to add an item without creating
# a brand-new list
