import json
import os

# Define Task class
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

# Save tasks to JSON
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from JSON
def load_tasks(filename="tasks.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return [Task(**data) for data in json.load(f)]

# Add a new task
def add_task(tasks):
    print("\n📝 Add New Task")
    title = input("Enter title: ")
    description = input("Enter description: ")
    category = input("Enter category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("✅ Task added successfully!")

# View all tasks
def view_tasks(tasks):
    print("\n📋 Your Tasks")
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔️ Done" if task.completed else "❌ Pending"
        print(f"{i}. [{status}] {task.title} | {task.category}\n   {task.description}")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].mark_completed()
            print("✅ Task marked as completed.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Deleted task: {removed.title}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main Menu Loop
def main():
    tasks = load_tasks()
    while True:
        print("\n========= Personal To-Do List =========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("💾 All changes saved. Exiting...")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
