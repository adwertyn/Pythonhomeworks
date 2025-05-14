even_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #the list has even number of elements
odd_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] #the list has odd number of elements
middle_even = (even_list[len(even_list)//2-1], even_list[len(even_list)//2]) #middle elements of even list
middle_odd = odd_list[len(odd_list)//2] #middle element of odd list
#print result for even
print(middle_even)
#print result for odd
print(middle_odd)
