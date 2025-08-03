from src.core.agent import extract_task
from src.core.planner import save_task_structured
from src.core.calendar_link import generate_gcal_link

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
            gcal_link = generate_gcal_link(task_info["description"], task_info["datetime"])
            print(f"\n📅 Add this to your Google Calendar:\n🔗 {gcal_link}\n")
        else:
            print(f"⚠️ AI returned invalid JSON: {task_info['error']}")
    else:
        print("🤔 Sorry, I couldn't understand. Try rephrasing.")
