import os

FILE_NAME = "tasks.txt"


# ----------------------------
# Load Tasks
# ----------------------------
def load_tasks():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks


# ----------------------------
# Save Tasks
# ----------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# ----------------------------
# Add Task
# ----------------------------
def add_task(tasks):
    task = input("Enter new task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# ----------------------------
# View Tasks
# ----------------------------
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n------ YOUR TASKS ------")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("------------------------")


# ----------------------------
# Update Task
# ----------------------------
def update_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to update: "))

        if 1 <= task_no <= len(tasks):
            new_task = input("Enter updated task: ")
            tasks[task_no - 1] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ----------------------------
# Delete Task
# ----------------------------
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f'"{deleted}" deleted successfully!')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ----------------------------
# Menu
# ----------------------------
def display_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("================================")


# ----------------------------
# Main Program
# ----------------------------
def main():
    tasks = load_tasks()

    while True:

        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                add_task(tasks)

            elif choice == 2:
                view_tasks(tasks)

            elif choice == 3:
                update_task(tasks)

            elif choice == 4:
                delete_task(tasks)

            elif choice == 5:
                print("\nThank you for using To-Do List!")
                break

            else:
                print("Please choose between 1 and 5.")

        except ValueError:
            print("Invalid input! Enter a number.")


if __name__ == "__main__":
    main()