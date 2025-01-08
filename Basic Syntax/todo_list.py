class TodoList:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully.")

    def remove_task(self, task):
        """Remove a task from the list."""
        for t in self.tasks:
            if t['task'] == task:
                self.tasks.remove(t)
                print(f"Task '{task}' removed successfully.")
                return
        print(f"Task '{task}' not found in the list.")

    def mark_completed(self, task):
        """Mark a task as completed."""
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True
                print(f"Task '{task}' marked as completed.")
                return
        print(f"Task '{task}' not found in the list.")

    def list_tasks(self):
        """List all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\nTo-Do List:")
        for index, t in enumerate(self.tasks, start=1):
            status = "Completed" if t['completed'] else "Pending"
            print(f"{index}. {t['task']} - {status}")

    def clear_tasks(self):
        """Clear all tasks from the list."""
        self.tasks.clear()
        print("All tasks have been cleared.")

# Main loop to interact with the To-Do List app
def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List All Tasks")
        print("5. Clear All Tasks")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_completed(task)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
