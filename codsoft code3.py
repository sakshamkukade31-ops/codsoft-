# To-Do List Application

tasks = []

while True:

    print("\n------ TO DO LIST ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add a new task
    if choice == "1":
        task = input("Enter task name: ")

        task_data = {
            "task": task,
            "completed": False
        }

        tasks.append(task_data)
        print("Task added successfully!")

    # Display all tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nCurrent Tasks:")

            for i in range(len(tasks)):
                if tasks[i]["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{i+1}. {tasks[i]['task']} - {status}")

    # Update existing task
    elif choice == "3":

        task_no = int(input("Enter task number to update: "))

        if task_no >= 1 and task_no <= len(tasks):

            new_task = input("Enter updated task: ")
            tasks[task_no - 1]["task"] = new_task

            print("Task updated successfully!")

        else:
            print("Invalid task number!")

    # Delete a task
    elif choice == "4":

        task_no = int(input("Enter task number to delete: "))

        if task_no >= 1 and task_no <= len(tasks):

            tasks.pop(task_no - 1)
            print("Task deleted successfully!")

        else:
            print("Invalid task number!")

    # Mark task as completed
    elif choice == "5":

        task_no = int(input("Enter task number to complete: "))

        if task_no >= 1 and task_no <= len(tasks):

            tasks[task_no - 1]["completed"] = True
            print("Task marked as completed!")

        else:
            print("Invalid task number!")

    # Exit program
    elif choice == "6":

        print("Exiting the application...")
        break

    else:
        print("Please enter a valid choice!")