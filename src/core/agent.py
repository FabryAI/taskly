import requests
import json
import re
import os
from datetime import datetime
from dotenv import load_dotenv

# 📥 Load environment variables from .env file (useful in development)
load_dotenv()

# 🔐 Load your API Key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# 🌍 API endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# 🤖 Choose the model to use (must be supported by OpenRouter)
MODEL = "mistralai/mistral-7b-instruct"

def extract_task(text: str) -> dict:
    """
    Call an AI model via OpenRouter API to extract task details from a user message.
    Returns a dictionary with 'intent', 'description', and 'datetime' keys.
    """
    today_str = datetime.now().strftime("%Y-%m-%d")

    # 🧠 Prompt sent to the model
    prompt = f"""
    Today is {today_str}.
    You are an intelligent task assistant.
    Extract the task from the following command and return ONLY the JSON object in this exact format:

    {{
    "intent": "add_task",
    "description": "...",
    "datetime": "ISO 8601 format"
    }}

    Command: "{text}"
    JSON:
    """


    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    print("🔍 Sending prompt to remote AI...")

    try:
        response = requests.post(API_URL, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print("📤 Response from AI:")
        print(reply)

        # 🧾 Extract JSON block
        json_block = re.search(r"\{.*\}", reply, re.DOTALL)
        if json_block:
            return json.loads(json_block.group())
        else:
            return {"error": "No JSON found in response"}

    except Exception as e:
        return {"error": str(e)}
