tasks = []

def add_task(task):
    if not task.strip():
        raise ValueError("Task cannot be empty.")
    tasks.append(task.strip())
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(number):
    if not tasks:
        print("No tasks to delete.")
        return

    if number < 1 or number > len(tasks):
        raise ValueError("Invalid task number.")

    deleted = tasks.pop(number - 1)
    print(f"Deleted task: {deleted}")