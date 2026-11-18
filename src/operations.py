# Task action functions
# Add  |  Complete  |  Delete/Handler

def add(tasks: list, task: str) -> None:
    if task:
        new_task = task.capitalize()
        print("Task added..")
        tasks.append(new_task)
    else:
        print("Task cannot be empty.")

def complete():
    pass

def delete(tasks: list, option: int) -> str:
        option -= 1
        removed_task = tasks.pop(option)
        return removed_task

# Handle deleting process
# Checking if input is a task number
def handle_delete(tasks: list) -> None:
    if tasks:
        task_number = input(f"Choose a task:  ")
        if task_number.isdigit():
            option = int(task_number)
        else:
            option = 0
            print("Must be a number.")
            return 
          
        is_valid_number: bool = 1 <= option <= len(tasks)
        if is_valid_number:
            deleted_task: str = delete(tasks, option)
            print(f'"{deleted_task}" was removed.')
        else:
            print("Invalid input.")
    else:
        print("Current list is empty.")