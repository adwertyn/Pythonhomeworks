#Asking User numbers separated with space
list_of_numbers = list(map(int,input("Enter numbers with spaces: ").split()))

#Finding and printing lagest one
print("Largest element is",max(list_of_numbers))