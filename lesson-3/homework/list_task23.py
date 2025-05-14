#Given intagers list
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = [] #Array to collect odd numbers

#Separating odd numbers and add them to odd_list
for i in  old_list:
    if i % 2 == 0:
        odd_list.append(i)
        

print("Only odd numbers:", odd_list) #<= Result