# Function to check Prime number
def Prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Loop to provide Prime numbers betweem 1 and 100
for i in range(1,101,1):  
    if Prime(i):
        print(i)