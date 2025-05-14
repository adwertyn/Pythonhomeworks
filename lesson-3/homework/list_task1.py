#Given list for counting element in it
given_list = [1, 2, 3, 4, 2, 2, 5, 6, 2, 7, 9, 5, 4, 4, 8, 10]

#Asking user number
target_element = int(input("Enter the number please: "))

#counting how many times the element appears in the list.
counting = given_list.count(target_element)

#Printing result
print(f"The element {target_element} appears {counting} times in the list.")