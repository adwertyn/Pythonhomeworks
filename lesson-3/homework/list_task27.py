my_list = [10, 25, 7, 40, 18, 33, 5] #given list
start = 1 #start index
end = 5 #end index for sublist

sublist = my_list[start:end] #separate sublist
max_value = max(sublist) #find max value

#Print sublist and max value
print("Sublist:", sublist)
print("Maximum value in sublist:", max_value)
