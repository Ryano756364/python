shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list

print(id(shopping_list))  # 2195850221504
print(id(another_list))  # 2195850221504

shopping_list += ["cookies"]
print(shopping_list)  # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
print(id(shopping_list))  # 2198131660736

# lists are mutable and Python was able to add an item without creating
# a brand-new list

# how many lists are on this screen?
# answer: only 1 list
# both names are bound to the same object

a = b = c = d = e = f = another_list  # 8 references to the same list

print(a)  # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
print("Adding cream")
b.append(("cream"))
print(c)  # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'cream']
print(d)  # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'cream']
