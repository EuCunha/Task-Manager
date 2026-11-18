from typing import Final
import src.storage as storage
import src.operations as op
import src.ui as ui

FILE_PATH: Final = 'data/tasks.json'

# Main loop
def main(file, tasks) -> None:

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
            storage.save(file, tasks)
        elif menu_choice == '3':
            op.handle_delete(tasks)
            storage.save(file, tasks)
        else: print("Not an option.")


if __name__ == "__main__":
    tasks = storage.load(FILE_PATH)
    main(FILE_PATH, tasks)
    