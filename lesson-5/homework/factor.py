#Ask user number
number = int(input("Enter a positive integer: "))

# loop run from 1 to number
for i in range(1,number+1,1):  
    #check i is factor of number
    if number % i == 0:     
        print(f'{i} is a factor of {number}')
