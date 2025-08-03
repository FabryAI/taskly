import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TASK_FILE = BASE_DIR / "data" / "tasks.json"

def save_task_structured(task: dict, filename: Path = TASK_FILE):
    filename.parent.mkdir(parents=True, exist_ok=True) 
    if filename.exists():
        try:
            with open(filename, "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
    else:
        tasks = []

    tasks.append(task)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def show_tasks():
    """
    Print a sorted list of all tasks from the JSON file.
    """
    if not TASK_FILE.exists():
        print("📭 No tasks found.")
        return

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        tasks = json.load(f)

    tasks_sorted = sorted(tasks, key=lambda x: x["datetime"] or "")
    print("\n📋 Task List:")
    for t in tasks_sorted:
        print(f"🗓️  {t['datetime'] or '???'} → {t['description']}")
