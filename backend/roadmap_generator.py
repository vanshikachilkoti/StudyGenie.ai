# backend/roadmap_generator.py

import requests
from config import HF_API_KEY

def build_prompt(data):
    topic = data["topic"]
    subtopics = data.get("subtopics", "")
    level = data["level"]
    goal = data["goal"]
    hours = data["hours"]
    deadline = data["deadline"]
    formats = ", ".join(data["formats"])
    learning_style = data["learning_style"]

    return f"""
You are an expert curriculum planner.

Create a personalized weekly study roadmap for the following user:

- Topic: {topic}
- Subtopics: {subtopics if subtopics else 'None specified'}
- Proficiency level: {level}
- Goal: {goal}
- Deadline: {deadline}
- Weekly Study Time: {hours} hours/week
- Preferred Content Types: {formats}
- Learning Style: {learning_style}

The roadmap should:
1. Be divided by week (Week 1, Week 2, etc.)
2. Use the preferred content formats
3. Include estimated time per task each week
4. Be practical, engaging, and goal-focused
5. Match the user’s learning style
6. Stay within the user’s weekly time commitment

Respond in a **well-formatted email-style** message.
"""

def generate_roadmap(data):
    prompt = build_prompt(data)

    url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 800,
            "temperature": 0.7,
            "top_p": 0.9,
            "return_full_text": False
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"❌ Hugging Face API Error: {response.status_code} - {response.text}")

    result = response.json()

    # Always validate the structure
    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]
    else:
        raise Exception("❌ Unexpected response format from Hugging Face API.")
