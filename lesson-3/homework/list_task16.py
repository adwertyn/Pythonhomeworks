# Given a list of integers
lst = [10, 11, 12, 13, 14, 15, 16, 17]

count_odd = 0
#Count how many odd numbers
for i in lst:
    if i % 2 == 1:
        count_odd += 1
        
#Print Count odd Numbers:
print(count_odd) 