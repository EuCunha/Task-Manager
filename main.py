import json
from typing import Final

FILE_PATH: Final = 'data//tasks.json'

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
    return data_file.append(new_task)

def complete():
    pass

def delete(data_file: list, option: str) -> None:
    try:
        option = int(option) - 1
        data_file.pop(option)
    except IndexError as e:
        print(e)




tasks = load(FILE_PATH)
view(tasks)

# new_task = input("option | task > ")
# add(tasks, new_task)
# delete(tasks, new_task)
# save(FILE_PATH, tasks)
# print(len(tasks))