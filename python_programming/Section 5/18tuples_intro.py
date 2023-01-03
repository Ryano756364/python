t = "a", "b", "c"
print(t)  # ('a', 'b', 'c')
# notice the parenthesis instead of brackets []

t = ("a", "b", "c")  # this works too and there are times when () are necessary
print(t)

name = "Ryan"
year = 2023
print(name, year, "Python", 2022)  # Ryan 2023 Python 2022
print((name, year, "Python", 2022))  # (Ryan 2023 Python 2022)
# 1 instance of needing () is when it's passed as a literal argument
# such as the line immediately preceding this one

# may be good practice to always use () with Tuples

# Tuples are immutable unlike Lists
# indexing of Tuples is the same as Lists
# you still use [] to index them (watch this as it can be confusing)
# Tuples use less memory than Lists
# Tuples protect integrity of data

# you can turn a Tuple into a List as below:
list_form = list(t)
print(list_form)  # ['a', 'b', 'c']

# unpacking a Tuple
list_of_letters = ["a", "b", "c"]
x, y, z = list_of_letters
print(list_of_letters)  # ['a', 'b', 'c']
print(x, y, z)  # a b c
# another advantage is Tuple's are ALWAYS unpacked successfully
# (when program works of course and there aren't too many variables
# to upack into the Tuple)
