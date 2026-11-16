import json
from typing import Final

FILE_PATH: Final = 'data/tasks.json'

# Storage functions
# Load  |  Save
def load(file: str) -> dict | list:
    assert file.endswith('.json'), 'Expected a .json file.'
    
    try:
        with open(file, mode="r", encoding="utf-8") as f:
            tasks: dict | list = json.load(f)
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save(file: str, tasks: list) -> None:
    with open(file, mode="w", encoding="utf-8") as f:
        json.dump(tasks, f)

# Task action functions
# View  |  Add  |  Complete  |  Delete
def view(tasks: list) -> None:
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f'{i} -> {task}')
    else:
        print("Current list is empty") 

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
        view(tasks)
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

# Main loop
def main(filename, tasks) -> None:
    
    print("+--- TASK MANAGER --+")
    print("=====================")
    print("1. View")
    print("2. Add")
    print("3. Delete")
    print("4. Quit")

    while True:
        menu_choice = input("Enter a option: ").strip()

        if menu_choice == '4':
            break
        elif menu_choice == '1':
            view(tasks)
        elif menu_choice == '2':
            new_task = input("Enter a task: ").strip()
            add(tasks, new_task)
        elif menu_choice == '3':
            handle_delete(tasks)
        else: print("Not an option.")


if __name__ == "__main__":
    tasks = load(FILE_PATH)
    main(FILE_PATH,tasks)
    save(FILE_PATH, tasks)