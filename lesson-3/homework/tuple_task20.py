orginal_tuple = (1, 2, 3, 4, 5, 6, 7, 9, 1, 0, 15, 20, 15, 1, 15,)
sub_size = 3     # Number of elements in each sublist

nested_tuple = []   #not tuple because unable to use append with it
for i in range(0, len(orginal_tuple), sub_size):
    nested_tuple.append(orginal_tuple[i:i+sub_size]) #Make sublists 
    

print(tuple(nested_tuple)) #Print in tuple