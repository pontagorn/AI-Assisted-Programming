def main():
    todo_list = []
    while True:
        command = input("Enter command (add/list/remove/exit): ").strip()
        if command.lower() == "exit":
            print("See you later!")
            break
        elif command.lower().startswith("add "):
            task = command[4:].strip()
            if task:
                todo_list.append(task)
                print(f'Added: "{task}"')
            else:
                print("Please specify a task to add.")
        elif command.lower() == "list":
            if not todo_list:
                print("No tasks in the list.")
            else:
                print("+-----+----------------------------+")
                print("| No. | Task                       |")
                print("+-----+----------------------------+")
                for idx, task in enumerate(todo_list, 1):
                    display_task = (task[:26] + '...') if len(task) > 29 else task
                    print(f"| {str(idx).ljust(3)} | {display_task.ljust(26)} |")
                print("+-----+----------------------------+")
        elif command.lower().startswith("remove "):
            try:
                num = int(command[7:].strip())
                if 1 <= num <= len(todo_list):
                    removed = todo_list.pop(num - 1)
                    print(f'Removed: "{removed}"')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please specify a valid task number to remove.")
        else:
            print("Unknown command. Please use add/list/remove/exit.")

if __name__ == "__main__":
    main()