def is_prime(num):
    if num < 2: 
        return False  # Not prime if less than 2
    for i in range(2, int(num**0.5) + 1): # Loop to check whether the number has any divisors
        if num % i == 0: 
            return False  # Not prime cause it has divisor other than 1 and itself
    return True  # Prime if no divisors found

number = int(input("Enter the number: "))

#Call is_prime function and print result
print(is_prime(number))
