def add_employee():
    while True:
        employee_id = input("Enter Employee ID: ")
        if employee_id.isdigit():
            break
        else:
            print("Please enter a valid numeric Employee ID.")

    while True:
        name = input("Enter Name: ")
        if name.isdigit():
            print("Enter a string, not a number!")
        else:
            break

    while True:
        position = input("Enter Position: ")
        if position.isdigit():
            print("Enter a string, not a number!")
        else:
            break

    salary = input("Enter Salary: ")

    with open("employees.txt", "a") as file:
        file.write(f"{employee_id}, {name}, {position}, {salary}\n")
    print("Employee added successfully!\n")

def display_records():
    with open("employees.txt", 'r') as file:
        records = file.readlines()
        if not records:
            print("No employee records")
        else:
            print("Employee Records:")
            for record in records:
                print(record.strip())
def search_info():
    employee_id = input("Enter Employee ID to search: ")
    with open("employees.txt", "r") as file:
        for line in file:
            if line.startswith(employee_id + ","):
                print("Employee Found: ", line.strip())
                found = True
                break
    if not found:
        print("Employee not found.\n")


while True:
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