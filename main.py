from src.core.agent import extract_task
from src.core.planner import save_task_structured


print("🤖 Taskly is active. Type a task like 'Tomorrow at 3pm meeting with Marco'. Type 'bye bye' to exit.")

while True:
    user_input = input("👤 You: ")

    if user_input.lower() in ["bye", "bye bye", "exit", "quit"]:
        print("👋 See you next time!")
        break

    task_info = extract_task(user_input)

    if task_info.get("intent") == "add_task":
        if "error" not in task_info:
            save_task_structured(task_info)
        else:
            print(f"⚠️ L'AI non ha generato un JSON valido: {task_info['error']}")

    else:
        print("🤔 Sorry, I couldn't understand. Try rephrasing.")
