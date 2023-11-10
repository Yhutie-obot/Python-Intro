# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found:", task)

# Function to list all tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

# Main program loop
while True:
    print("\nOptions:")
    print("Enter 'add' to add a task")
    print("Enter 'remove' to remove a task")
    print("Enter 'list' to list all tasks")
    print("Enter 'exit' to exit the program")

    user_input = input("Enter a task:\n")

    if user_input == "exit":
        break
    elif user_input == "add":
        task = input("Enter a task: ")
        add_task(task)
    elif user_input == "remove":
        task = input("Enter a task to remove: ")
        remove_task(task)
    elif user_input == "list":
        list_tasks()
    else:
        print("Invalid input. Please try again.")
