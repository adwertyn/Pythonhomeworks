#input from the user, split it by spaces
list1 = list(map(int, input("Enter first list of numbers: ").split()))

#input from the user, split it by spaces
list2 = list(map(int, input("Enter second list of numbers: ").split()))

#unique_list to store unique elements using symmetric_difference() 
unique_list = set(list1).symmetric_difference(set(list2))

#Print uniue set
print(unique_list)
