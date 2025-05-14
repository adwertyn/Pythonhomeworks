#Asking user numbers with space in tuple
user_tuple = tuple(map(int,input("Enter numbers with spaces: ").split()))
#Asking user number to repeat
number = int(input("Enter single number: "))

new_tuple = ()

for i in user_tuple:
    new_tuple += (i,) * number 

#Result
print(new_tuple)