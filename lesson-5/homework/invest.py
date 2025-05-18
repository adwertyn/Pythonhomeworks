def invest(amount, rate, years):
    for year in  range(1,years+1, 1):       #loop calculate for each year
        print(f"year {year}: {round(amount  * (rate+1) ** year, 2)}")   #print annual value of user's profit

#Ask user amount, rate, and year
amount = float(input("Enter how much money you invested: "))
rate = float(input("Enter the rate for a year: "))
# User needs to enter integer for year
try:
    years = int(input("Enter how many years you signed the contract for: "))
except:
    years = int(input("Please enter integer type for year: "))
# Call invest() function
invest(amount, rate, years)