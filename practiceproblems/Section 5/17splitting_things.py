panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)  # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

panagram = """The quick brown fox 
jumps\t over the lazy dog"""
print(words)  # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# no difference

numbers = "9,223,372,036,865"
print(numbers.split(","))  # ['9', '223', '372', '036', '865']
# when you split a string, you get a string in return

values = "".join(numbers)
print(values)  # 9,223,372,036,865


# turn this into a list of ints
string_numbers = ['9', '223', '372', '036', '865']
int_numbers = []
for string_number in string_numbers:
    int_numbers.append(int(string_number))
print(int_numbers)