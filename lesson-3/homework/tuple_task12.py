my_tuple = (5, 1, 9, 3, 9, 2)

unique_values = sorted(list(set(my_tuple)))
second_largest = unique_values[-2] if len(unique_values) > 1 else None

print(second_largest) 