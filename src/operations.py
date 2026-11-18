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

def delete(tasks: list, option: int) -> str:
        return tasks.pop(option - 1)    