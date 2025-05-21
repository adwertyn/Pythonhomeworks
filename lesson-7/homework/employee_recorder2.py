class Manager_main:
    def __init__ (self):
        self.employees = {}
        self.load_data()
        
    def load_data(self):
        with open("employees.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 4:
                    emp_id, name, position, salary = parts
                    self.employees[emp_id] = (name, position, salary)
    def save_data(self):
        with open("employees.txt", "w") as file:
            for emp_id, (name, position,salary) in self.employees.items():
                file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    def add_employee(self):
        while True:
            emp_id = input("Enter Employee ID: ")
            if emp_id.isdigit() and emp_id not in self.employees:
                break
            print("Invalid or duplicate ID. Try again.")

        while True:
            name = input("Enter Name: ")
            if not name.isdigit():
                break
            print("Name should not be numeric.")

        while True:
            position = input("Enter Position: ")
            if not position.isdigit():
                break
            print("Position should not be numeric.")

        salary = input("Enter Salary: ")
        self.employees[emp_id] = (name, position, salary)
        print("Employee added successfully!\n")
    def display_records(self):
        if not self.employees:
            print("No employee records.\n")
        else:
            print("Employee Records:")
            for emp_id, (name, position, salary) in self.employees.items():
                print(f"{emp_id}, {name}, {position}, {salary}")
            print()

    def search_info(self):
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in self.employees:
            name, position, salary = self.employees[emp_id]
            print(f"Employee Found: {emp_id}, {name}, {position}, {salary}\n")
        else:
            print("Employee not found.\n")

    def update_record(self):
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in self.employees:
            print(f"Current Record: {emp_id}, {', '.join(self.employees[emp_id])}")
            name = input("Enter new name: ")
            position = input("Enter new position: ")
            salary = input("Enter new salary: ")
            self.employees[emp_id] = (name, position, salary)
            print("Employee updated successfully!\n")
        else:
            print("Employee ID not found.\n")

    def delete_record(self):
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee record deleted!\n")
        else:
            print("Employee ID not found.\n")
            
"""=== Code starts here ==="""
with open('employees.txt', 'w') as file:
    pass
manager = Manager_main()

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
        manager.add_employee()
    elif option == 2:
        manager.display_records()
    elif option == 3:
        manager.search_info()
    elif option == 4:
        manager.update_record()
    elif option == 5:
        manager.delete_record()
    elif option == 6:
        manager.save_data()
        print("Good bye!🖐️")
        break
    else:
        print("Choose a number(1-6)")