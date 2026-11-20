# Task action functions
# Add  |  Complete  |  Delete/Handler

def add(tasks: list, task: str) -> str:
    if task:
        new_task = task.capitalize()
        tasks.append(new_task)
        return "Task added."
    else:
        return "Task cannot be empty."

def complete():
    pass

## TODO
def delete(tasks: list, option: str) -> str:
    # if option.isdigit():
    #     index = int(option)
    return tasks.pop(option - 1)
    # if option in tasks:
    #     removed = tasks.remove(option)
    #     return removed