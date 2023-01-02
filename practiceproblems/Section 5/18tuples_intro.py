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
