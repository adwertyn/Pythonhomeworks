my_dict = {'a': 1, 'b': 5, 'c': 2}
filtered = {k: v for k, v in my_dict.items() if v > 2}
print(filtered)  # Output: {'b': 5}
