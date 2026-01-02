import json
import os

# File to store the to-do list
FILE_NAME = 'todo_list.json'

def load_tasks():
    """Load tasks from file if it exists."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks in the list.")
        return
    for i, task in enumerate(tasks, 1):
        status = "[✓]" if task['done'] else "[ ]"
        print(f"{i}. {status} {task['description']}")  # Corrected: No extra parentheses

def add_task(tasks):
    """Add a new task."""
    description = input("Enter task description: ").strip()
    if description:
        tasks.append({'description': description, 'done': False})
        print("Task added.")
    else:
        print("Task description cannot be empty.")

def mark_done(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the app."""
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()