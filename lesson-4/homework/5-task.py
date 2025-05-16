i = True
while True:
    password = input("Enter the password: ")
    #Check lenght of password is correct
    if len(password) < 8:
        print("Password is too short.")
    # Check for at least one uppercase letter
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    # If both conditions are satisfied
    else:
        print("Password is strong.")
        break
