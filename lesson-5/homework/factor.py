#Ask user number
number = int(input("Enter a positive integer: "))

# loop run from 1 to number
for factor in range(1,number+1,1):  
    if number % factor == 0:     #check is the number divisible by a factor?
        print(f'{factor} is a factor of {number}')
