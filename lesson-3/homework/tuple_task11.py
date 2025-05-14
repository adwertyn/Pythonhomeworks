#Given tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5)
#Target to find indexes
target = 2

indexes = [] #list to collect 
for i in range(len(my_tuple)):
    if my_tuple[i] == target:
        indexes.append(i)  #containing indexes of target
print(indexes)