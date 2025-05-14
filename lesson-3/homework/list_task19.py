given_list = [10, 20, 30, 40, 30, 50]

old = 40 
new = 100
#replacing old with new value
if old in given_list:
    index_of_old = given_list.index(old) # find index of old value
    given_list[index_of_old] = new
print(given_list)
    