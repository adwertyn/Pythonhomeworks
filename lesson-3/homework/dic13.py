my_dict = {'a': 1, 'b': 2}
inverted = {v: k for k, v in my_dict.items()}
print(inverted)  # Output: {1: 'a', 2: 'b'}
