#Given list
my_list = [1, 2, 3]
count = 3 #how many times should repeat

repeated_list = []
for item in my_list:
    repeated_list.extend([item] * count) #Extend for add several items to list

print("Repeated list:", repeated_list) #Print answer
