# function starts with def, then name, then ()
# x, y are parameters (or formal parameters)
def multiply(x, y):
    result = x * y
    return result


# PEP 8 wants two blank lines at end of function
# providing arguments is known as "passing arguments"
print(multiply(10, 4))  # 40

# loop example
for val in range(1,5):
    two_times = multiply(val, 2)
    print(two_times)  # 2, 4, 6, 8

# Python arguments are passed by assignment

# Similar to pass by reference, when passing a mutable object
# For immutable -> pass by value
# but these two don't have much meaning in Python

# Look into "Call by Sharing"

# Positional Arguments -> arguments assigned to parameterrs in order
# that they appear

# Scope -> where a variable exists

def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string  # or use more concise code below
    return string[::-1].casefold() == string.casefold()

print(is_palindrome("foOf"))
print(is_palindrome("fOod"))
