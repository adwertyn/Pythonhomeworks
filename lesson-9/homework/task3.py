import json
import csv

JSON_FILE = 'tasks.json'
CSV_FILE = 'tasks.csv'
def load_tasks():
    try:
        with open(JSON_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"{JSON_FILE} not found. Creating a new file with empty list.")
        with open(JSON_FILE, 'w') as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {JSON_FILE}. Please check if the file contains valid JSON.")
        return []


def save_tasks(tasks):
    with open(JSON_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nAll Tasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    average_priority = sum(t['priority'] for t in tasks) / total if total else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {average_priority:.2f}")

def convert_to_csv(tasks):
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Task', 'Completed', 'Priority'])
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
    print(f"\nTasks exported to {CSV_FILE}")

if __name__ == '__main__':
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)

    for task in tasks:
        if task['id'] == 1:
            task['completed'] = True

    save_tasks(tasks)
    convert_to_csv(tasks)
