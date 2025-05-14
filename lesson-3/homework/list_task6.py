#function to get first one or return it is empty

def first_element(lst):
    if lst:
        return lst[0]
    else:
        return "The list is empty."
#Given list
my_list = [10, 20, 30]
print("First element:", first_element(my_list))

empty_list = []
print("First element:", first_element(empty_list))
