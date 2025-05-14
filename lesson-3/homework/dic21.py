my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_value)  # Output: {'a': 1, 'b': 2, 'c': 3}
