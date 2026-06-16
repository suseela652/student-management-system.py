tasks = []

while True:
    print("\n===== TODO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])

            try:
                num = int(input("Enter task number to remove: "))
                if num >= 1 and num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print("Removed:", removed)
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting Todo App...")
        break

    else:
        print("Invalid choice. Try again.")