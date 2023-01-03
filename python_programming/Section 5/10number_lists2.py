# create list with empty literal
empty_list = []

# list of values in square brackest
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# can concatenate
numbers = even + odd
print(numbers)  # [2, 4, 6, 8, 1, 3, 5, 7, 9]

# can create a list by returning one as well
# remembered sorted creates new list
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)  # [2, 4, 6, 8, 1, 3, 5, 7, 9]

# when you create new list, object type of original list will be same
# string to string
digits = sorted ("432985617")
print(digits)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

list_digits = list("432985617")
print(list_digits)  # ['4', '3', '2', '9', '8', '5', '6', '1', '7']

print(numbers is list_digits)  # False
# same list, yes, but different 'values'

# more_numbers = numbers[:]      this is one way to do it in Python 2
more_numbers = numbers.copy()  # there is a better way to do this
print(more_numbers)
print(more_numbers is numbers)
