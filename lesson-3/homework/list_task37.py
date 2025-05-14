my_list = [-5, 10, -3, 7, 0, 4]

negative_sum = 0 #variable to calculate sum of negative numbers
for i in my_list:
    if i > 0:
        negative_sum += i

print("Sum of negative numbers:", negative_sum)
