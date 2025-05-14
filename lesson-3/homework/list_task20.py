#Given list
my_list = [10, 20, 30, 40, 30, 50]
my_list = list(set(my_list)) #remove duble elements
my_list.sort() #sorting to find it easy

print("Second largest element:", my_list[-2] if len(my_list) >= 2 else my_list[0])  #print second largest element