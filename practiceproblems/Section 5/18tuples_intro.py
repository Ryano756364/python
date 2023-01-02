t = "a", "b", "c"
print(t)  # ('a', 'b', 'c')
# notice the paranthesis instead of brackets []

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

# you can turn a Tupple into a List as below:
list_form = list(t)
print(list_form)  # ['a', 'b', 'c']
