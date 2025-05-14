my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
step = 2  # Number of positions to rotate

# Use negative slicing to rotate right
rotated_list = my_list[-step:] + my_list[:-step]

print("Rotated list:", rotated_list)