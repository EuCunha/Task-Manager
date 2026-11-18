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
