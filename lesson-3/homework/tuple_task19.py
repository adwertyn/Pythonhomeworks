old_tuple = (8, 1, 2, 6, 4, 5, 6, 5, 8, 9, 10, 1, 9, 3, 4)
target = 8
new_tuple = list(old_tuple).copy()
new_tuple.pop(new_tuple.index(target))
print(tuple(new_tuple))