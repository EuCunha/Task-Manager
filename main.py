from typing import Final
from src.storage import *
import src.operations as op
import src.ui as ui

FILE_PATH: Final = 'data/tasks.json'

# Main loop
def main(tasks) -> None:

    ui.menu()

    while True:
        menu_choice = input("Enter a option: ").strip()

        if menu_choice == '4':
            break
        elif menu_choice == '1':
            ui.view(tasks)
        elif menu_choice == '2':
            new_task = input("Enter a task: ").strip()
            op.add(tasks, new_task)
        elif menu_choice == '3':
            op.handle_delete(tasks)
        else: print("Not an option.")


if __name__ == "__main__":
    tasks = load(FILE_PATH)
    main(tasks)
    save(FILE_PATH, tasks)