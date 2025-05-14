my_dict = {'a': 1, 'b': 2}
value = my_dict.get('b')  # returns 2
missing = my_dict.get('z', 'Not Found')  # returns default if key not found
print(value)
print(missing)
