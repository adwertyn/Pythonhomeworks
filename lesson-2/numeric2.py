#Input three numbers
n1 = float(input("Enter first number: ")) #What type of number wasn't mentioned to use, so I took float type
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

#Find maximum and minimum numbers
maximum_number = max(n1,n2,n3)
minimum_number = min(n1,n2,n3)

#Output answers
print("Maximum number is:", maximum_number)
print("Minimum number is:", minimum_number)