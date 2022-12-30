parrot = "Norwegian Blue"

print(parrot)  # Norwegian Blue

print(parrot[3])  # w
# python starts at position 0

print(parrot[-1])  # e
print(parrot[len(parrot) - 1])  # e

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[:6])  # Norweg

print(parrot[len(parrot) - 4])  # B
print(parrot[len(parrot) - 4:])  # Blue
print(parrot[len(parrot) - 4: len(parrot)])  # Blue
print(parrot[:])    # Norwegian Blue

# Negative indeces count from the end, not the beginning
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl
