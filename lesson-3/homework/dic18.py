from collections import defaultdict

my_dict = defaultdict(lambda: 'default')
my_dict['a'] = 1
print(my_dict['a'])  # Output: 1
print(my_dict['b'])  # Output: default
