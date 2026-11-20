# Manages all terminal printing, menu displays, and user input prompts.

def menu():
    print("+--- TASK MANAGER --+")
    print("=====================")
    print("1. View")
    print("2. Add")
    print("3. Delete")
    print("4. Quit")

def view(tasks: list) -> None:
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task.capitalize()}')
    else:
        print("Current list is empty") 

def get_input(prompt: str = "") -> str:
    if prompt:
        return input(f"{prompt}: ").strip()
    else: return input(">> ").strip()

## TODO: see what I can do later to improve this logic
def get_task_choice(tasks) -> str | None:
    choice = get_input("Choose a task")
    if choice:
        if choice.isdigit():
            if 1 <= int(choice) <= len(tasks):
                return choice
            elif choice in tasks:
                return choice
            else:
                print(f'"{choice}" index out of range.')
                return
        elif choice and choice not in tasks:
            print(f'"{choice}" not in tasks list.')
            return

        return choice
    print("Choice can't be empty.")
        

def show_message(arg):
    print(arg)
