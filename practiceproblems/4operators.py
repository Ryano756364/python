# 12 and 3 are technically expressions
a = 12
b = 3

# whenever we use the name 'a', Python will know we are referring to the value 12

# a + b is the expression
print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4 integer division, rounded down towards infinity
print(a % b)  # 0, remainder is 0

print()

for i in range(1, 4):
    print(i)  # prints 1, 2, 3

# // is needed for integer
# / will produce a float
# 1 is a literal value and also an expression
# a//b is an expression
for i in range(1, a // b):
    print(i)  # prints 1, 2, 3

print(a + b / 3 - 4 * 12)  # prints -35.0, uses operator precedence
