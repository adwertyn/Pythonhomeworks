#Given intagers list
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [] #Array to collect even numbers

#Separating even numbers and add them to even_list
for i in  old_list:
    if i % 2 == 0:
        even_list.append(i)
        

print("Only even numbers:", even_list) #<= Result