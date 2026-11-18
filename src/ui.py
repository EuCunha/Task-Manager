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
            print(f'{i} -> {task}')
    else:
        print("Current list is empty") 

def get_input(prompt: str = "") -> str:
    if prompt:
        return input(f"{prompt}: ").strip()
    else: return input(">> ").strip()

def get_task_choice(tasks) -> int | None:
    choice = get_input("Choose a task")
    if choice.isdigit():
        choice_num = int(choice)
    else:
        print("Must be a number.")
        return  
        
    if 1 <= choice_num <= len(tasks):
        return choice_num
    else: 
        print("Invalid input.")
        return

def show_message(arg):
    print(arg)
