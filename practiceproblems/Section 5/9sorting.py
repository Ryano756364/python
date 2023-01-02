# sort can sort any iterable object

pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)  # returns list in alphabetical order
# uppercase sorts before lowercase
# letters are duplicated

numbers = [2.3, 4.5, 8.7, 2.1, 0.5]
sorted_numbers = sorted(numbers)  # sorted returns new list
print(sorted(numbers))  # prints out in numerical order
print(numbers)  # prints out original numbers list

# difference between sort and sorted?

another_sorted_numbers = numbers.sort()  # sort -> sorts list in place compared to line 11
print(numbers)  # sorted list
print(another_sorted_numbers)  # None
# this is due to line 17 not returning any list

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)