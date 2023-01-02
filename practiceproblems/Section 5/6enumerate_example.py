# variable names don't matter
# enumerate is very usefully when you need the index
for t in enumerate("abcdefgh"):
    index, character = t
    print(t)
    print(index, character)

# t prints 8 tuples
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')
# (7, 'h')

# index, character prints
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g
# 7 h

index, character = (0, "a")
print(index, character)  # 0, a