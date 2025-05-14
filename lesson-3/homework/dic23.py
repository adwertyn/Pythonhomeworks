dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

common = set(dict1) & set(dict2)
print(len(common) > 0)  # Output: True
