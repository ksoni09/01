TASKS_FILE = "tasks.txt"

def read_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        print("No tasks found.")
        return []
    except Exception as e:
        print("An error occurred while reading tasks:", e)
        return []

def write_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved successfully!")
    except Exception as e:
        print("An error occurred while writing tasks:", e)

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)

def remove_task(task):
    tasks = read_tasks()
    if task in tasks:
        tasks.remove(task)
        write_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Task not found.")

def view_tasks():
    tasks = read_tasks()
    if tasks:
        print("\nTask List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks available.")

def main():
    print("Welcome to Task List Manager!")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting Task List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()