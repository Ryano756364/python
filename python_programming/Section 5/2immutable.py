result = True
another_result = result

print(id(result))  # 140731752946536 - may change if Python destroys
print(id(another_result))  # 140731752946536 - same here

result = False
print(id(result))  # 140731752946568

result = True
print(id(result))  # 140731752946536
