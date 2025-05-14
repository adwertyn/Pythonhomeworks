# Given list
my_list = [10, 25, 7, 40, 18, 33, 5, 12, 49]
index = 5 #index for remove
if 0 <= index < len(my_list):
    removed = my_list.pop(index) #Pop function remove element by index
    print("Removed element:", removed)
else:
    print("Index is out of range.")

print(my_list) #Updated list
