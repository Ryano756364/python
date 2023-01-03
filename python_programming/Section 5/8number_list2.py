even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# extend takes all the items and adds to list
even.extend(odd)
print(even)  # [2, 4, 6, 8, 1, 3, 5, 7, 9]

even.sort()
another_even = even
print(even)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

even.sort(reverse=True)
print(even)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]
# no new list was created, same list, just sorted


print(even)
print(another_even)  # note here that the list is in reverse order
# doesn't go by the first sort on line 9
# name points to value, not storing it

# fyi - not all mutable objects are sortable in Python
