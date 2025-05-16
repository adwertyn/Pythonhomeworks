#input from the user, split it by spaces
list1 = list(map(int, input("Enter first list of numbers: ").split()))

#input from the user, split it by spaces
list2 = list(map(int, input("Enter second list of numbers: ").split()))

#empty list to store unique elements
unique_list = []

#Loop for through each element in list1
for i in list1:
    # If the element is not in list2, it's unique to list1, so add to unique_list
    if i not in list2:
        unique_list.append(i)

# Loop for through each element in list2
for i in list2:
    # If the element is not in list1, it's unique to list2, so add to unique_list
    if i not in list1:
        unique_list.append(i)

# Print the list containing elements that are unique to either list1 or list2
print(unique_list)
