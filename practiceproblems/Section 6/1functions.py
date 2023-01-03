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
