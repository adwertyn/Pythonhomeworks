#function to get last one or return it is empty
def last_element(lst):
    if lst:
        return lst[-1]
    else:
        return "The list is empty."
#Given list
my_list = [10, 20, 30]
print("Last element:", last_element(my_list))

empty_list = []
print("Last element:", last_element(empty_list))
