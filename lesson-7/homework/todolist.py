import csv

class App:
    def __init__(self):
        self.tasks = {}
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('todoapp.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 5:
                        task_id, title, description, date, status = row
                        self.tasks[task_id] = (title, description, date, status)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('todoapp.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for task_id, (title, description, date, status) in self.tasks.items():
                writer.writerow([task_id, title, description, date, status])

    def add_task(self):
        while True:
            task_id = input("Enter New Task ID: ")
            if task_id.isdigit() and task_id not in self.tasks:
                break
            print("Invalid or duplicate ID. Try again.")
        while True:
            title = input("Enter Title: ")
            if not title.isdigit():
                break
            print("Title should not be numeric.")
        while True:
            description = input("Enter Description: ")
            if not description.isdigit():
                break
            print("Description should not be numeric.")
        date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter status of the task: ")
        self.tasks[task_id] = (title, description, date, status)
        print("Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No task records.\n")
        else:
            print("Task Records:")
            for task_id, (title, description, date, status) in self.tasks.items():
                print(f"{task_id}, {title}, {description}, {date}, {status}")
            print()

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        if task_id in self.tasks:
            print(f"Current Record: {task_id}, {', '.join(self.tasks[task_id])}")
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            date = input("Enter new date: ")
            status = input("Enter new status: ")
            self.tasks[task_id] = (title, description, date, status)
            print("Task updated successfully!\n")
        else:
            print("Task ID not found.\n")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task record deleted!\n")
        else:
            print("Task ID not found.\n")

    def filter_tasks(self):
        status_filter = input("Enter the status to filter by: ")
        found = False
        for task_id, (title, description, date, status) in self.tasks.items():
            if status.lower() == status_filter.lower():
                print(f"{task_id}, {title}, {description}, {date}, {status}")
                found = True
        if not found:
            print("No tasks with the given status found.\n")


user = App()

while True:
    print("""Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit""")
    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number between 1 and 8.\n")
        continue

    if option == 1:
        user.add_task()
    elif option == 2:
        user.view_tasks()
    elif option == 3:
        user.update_task()
    elif option == 4:
        user.delete_task()
    elif option == 5:
        user.filter_tasks()
    elif option == 6:
        user.save_data()
    elif option == 7:
        user.load_tasks()
        print("Tasks loaded successfully!\n")
    elif option == 8:
        print("Good bye! 🖐️")
        break
    else:
        print("Choose a number between 1 and 8.\n")
