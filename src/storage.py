import json
import pathlib

# Storage functions
# Load  |  Save
def load(file: str) -> list:
    assert file.endswith('.json'), 'Expected a .json file.'

    path = pathlib.Path(file)
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(file, mode="r", encoding="utf-8") as f:
            tasks: list = json.load(f)
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save(file: str, tasks: list) -> None:
    with open(file, mode="w", encoding="utf-8") as f:
        json.dump(tasks, f)