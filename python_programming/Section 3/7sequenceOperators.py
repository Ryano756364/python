string1 = "Happy "
string2 = "New "
string3 = "Year "

print(string1 + string2 + string3)  # Happy New Year

print(string1 * 2)  # Happy Happy

# operator precedence would apply here as well
print(string1 * 2 + "1")    # Happy Happy 1
# cannot be int otherwise an error would be thrown

today = "friday"
print("day" in today)   # True
print("fri" in today)   # True
print("the" in today)   # False
