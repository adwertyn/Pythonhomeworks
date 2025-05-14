original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group_size = 3  # Number of elements in each sublist

nested_list = []
for i in range(0,len(original_list), group_size):
    nested_list.append(original_list[i:i+group_size])

print("Nested list:", nested_list)
