# function signature notes using print example
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
import sys

x = 2
print(x)  # 2
print(x, sep=' ', end='\n', file=sys.stdout, flush=False)  # 2

# sep is how multiple objects are separated when print is called
# end can be useful when dealing with loops
