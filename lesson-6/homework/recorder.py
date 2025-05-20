def add_employee():  # Add a new employee
    while True:
        employee_id = input("Enter Employee ID: ")
        if employee_id.isdigit():  # ID must be numeric
            break
        else:
            print("Please enter a valid numeric Employee ID.")

    while True:
        name = input("Enter Name: ")
        if name.isdigit():  # Name must not be numeric
            print("Enter a string, not a number!")
        else:
            break

    while True:
        position = input("Enter Position: ")
        if position.isdigit():  # Position must not be numeric
            print("Enter a string, not a number!")
        else:
            break

    salary = input("Enter Salary: ")  # No validation for simplicity

    with open("employees.txt", "a") as file:
        file.write(f"{employee_id}, {name}, {position}, {salary}\n")  # Save to file
    print("Employee added successfully!\n")

def display_records():  # Show all records
    with open("employees.txt", 'r') as file:
        records = file.readlines()
        if not records:
            print("No employee records")
        else:
            print("Employee Records:")
            for record in records:
                print(record.strip())

def search_info():  # Search by ID
    employee_id = input("Enter Employee ID to search: ")
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(employee_id + ","):  # Match ID
                print("Employee Found: ", line.strip())
                found = True
                break
    if not found:
        print("Employee not found.\n")

def update_record():  # Update employee data
    employee_id = input("Enter Employee ID to update: ")
    updated = False
    with open('employees.txt', 'r') as file:
        lines = file.readlines()
    with open('employees.txt', 'w') as file:
        for line in lines:
            if line.startswith(employee_id+','):
                print("Current Record:", line.strip())
                name = input("Enter new name: ")
                position = input("Enter new position: ")
                salary = input("Enter new salary: ")
                file.write(f'{employee_id}, {name}, {position}, {salary}\n')  # Write updated
                updated = True
            else:
                file.write(line)
    if not updated:
        print("Employee ID not found.\n")

def delete_record():  # Delete employee by ID
    employee_id = input("Enter Employee ID to delete: ")
    deleted = False
    with open('employees.txt', 'r') as file:
        lines = file.readlines()
    with open('employees.txt', 'w') as file:
        for line in lines:
            if not line.startswith(employee_id+','):
                file.write(line)
            else:
                deleted = True
    
    if deleted:
        print("Employee record deleted!\n")
    else:
        print("Employee ID not found.\n")

# Main menu loop
while True:
    print('''1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit''')
    try:
        option = int(input("Choose an option (1-6): "))
    except ValueError:
        print("Invalid input. Enter a number between 1 and 6.")
        continue

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
        exit()  # Exit program
