from typing import Final
from sys import argv
import src.storage as storage
import src.operations as op
import src.ui as ui
import src.cli as cli

FILE_PATH: Final = 'data/tasks.json'

# Main loop
def main(file, tasks) -> None:

    if not len(argv) > 1:

        ui.menu()

        while True:
            menu_choice = ui.get_input()

            if menu_choice == '4':
                break
            elif menu_choice == '1':
                ui.view(tasks)
            elif menu_choice == '2':
                new_task = ui.get_input("Enter a task")
                add_task = op.add(tasks, new_task)
                ui.show_message(add_task)
                storage.save(file, tasks)
            elif menu_choice == '3':
                if tasks:
                    delete_choice = ui.get_task_choice(tasks)
                    if delete_choice is not None:
                        deleted = op.delete(tasks, delete_choice)
                        ui.show_message(deleted)
                        storage.save(file, tasks)
                else: print("Current list is empty.")

            else: print("Not an option.")
    else: 
        cli.run(tasks)
        storage.save(file, tasks)


if __name__ == "__main__":
    tasks = storage.load(FILE_PATH)
    main(FILE_PATH, tasks)
    