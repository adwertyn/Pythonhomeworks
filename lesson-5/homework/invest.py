def invest(amount, rate, years):
    for year in range(1, years + 1):
        print(f"Year {year}: {round(amount * (1 + rate) ** year, 2)}")

# Ask user for amount
while True:
    try:
        amount = float(input("Enter how much money you invested: "))
        if amount < 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Ask user for rate
while True:
    try:
        rate = float(input("Enter the rate for a year: "))
        if rate < 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Ask user for years
while True:
    try:
        years = int(input("Enter how many years you signed the contract for: "))
        if years < 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Call invest() function
invest(amount, rate, years)
