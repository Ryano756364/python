empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)  # [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

for number_list in numbers:
    for value in number_list:
        print(value)  # prints out each number on a new line


# search PEP 8 for style guide documentation
# code -> reformat can reformat code automatically for you in IntelliJ
# but this may not be a perfect reformat according to PEP 8
