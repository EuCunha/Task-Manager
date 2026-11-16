import json
from typing import Final

FILENAME: Final = 'tasks.json'

# Storage functions
# Load  |  Save
def load(file: str) -> dict | list:
    assert file.endswith('.json'), 'Expected a .json file.'
    
    try:
        with open(file, mode="r", encoding="utf-8") as f:
            task_data: dict | list = json.load(f)
        return task_data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save(file: str, data_file: list) -> None:
    with open(file, mode="w", encoding="utf-8") as f:
        json.dump(data_file, f)

# Task action functions
# View  |  Add  |  Complete  |  Delete
def view(data_file: list) -> None:
    for i, task in enumerate(data_file, start=1):
        print(f'{i} -> {task}')

def add(data_file: list, task: str) -> list:
    new_task = task.capitalize()
    data_file.append(new_task)
    return data_file




tasks = load(FILENAME)
view(tasks)

new_task = input("Enter a task: \n> ")
list_task = add(tasks, new_task)
view(tasks)
save(FILENAME, tasks)