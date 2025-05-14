#Given numbers list
given_list = [10, 11, 12, 13, 14, 15, 16, 17]

count_even = 0
#Count how many even numbers
for i in given_list:
    if i % 2 == 0:
        count_even += 1
        
#Print Count Even Numbers:
print(count_even) 