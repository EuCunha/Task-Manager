# Task action functions
# Add  |  Complete  |  Delete/Handler

def add(tasks: list, task: str) -> str:
    if task:
        new_task = task
        tasks.append(new_task)
        return "Task added."
    else:
        return "Task cannot be empty."

def complete():
    pass

## TODO
def delete(tasks: list, option: str) -> str:
    if option.isdigit():
        index = int(option)
        if not index > len(tasks):
            removed = tasks.pop(index - 1)
            return f'"{removed}" was removed.'
    if option in tasks:
        tasks.remove(option)
        return f'"{option}" was removed.'