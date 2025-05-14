my_list = [1, 3, 7, 3, 9, 3, 5]
target = 3
indices = [] #list contains target indexes
for i in range(len(my_list)):
    if my_list[i] == target:
        indices.append(i) #add index of target
print("Indices of", target, ":", indices) #Print result
