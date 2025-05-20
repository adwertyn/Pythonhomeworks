

def add_employee():
    while True:
        try:
            employee_id = input("Enter Employee ID: ")
            break
        except ValueError:
            print("You can't enter string. Please enter a number!")
            continue

    while True:
        name = input("Enter a name: ")
        if name.isdigit():
            print("Enter a string, not a number!")
            continue
        else:
            break
    while True:
        position = input("Enter a Position: ")
        if position.isdigit():
            print("Enter a string, not a number!")
            continue
        else:
            break
    


employees_file = open("employees.txt", mode='wt')

print('''1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit''')
option = int(input("Choose one option! Enter the number of option: "))
if option == 1:
    add_employee()
elif option == 2:
    display_records()
elif option == 3:
    search_info()
elif option == 4:
    update_record()
elif option == 5:
    delete_record()
else:
    exit()