import os
import requests
from dotenv import load_dotenv

load_dotenv()

class PersonaBuilder:
    def __init__(self):
        self.api_key = os.getenv("NVIDIA_API_KEY")
        self.endpoint = "https://integrate.api.nvidia.com/v1/chat/completions"
        self.model = "meta/llama3-70b-instruct"

    def build_persona(self, username, posts, comments):
        content = "\n\n---\n\n".join(posts + comments)
        prompt = self._generate_prompt(content)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a user researcher tasked with generating detailed user personas from Reddit activity."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 2048
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"❌ Error generating persona: {e}"

    def _generate_prompt(self, user_text):
        return (
        "You are a user researcher creating a structured user persona from Reddit activity. "
        "For each attribute (age, location, habits, goals, etc.), include the exact Reddit post/comment used to infer it, directly under the trait.\n\n"
        "Use this format:\n\n"
        "## Name: Reddit alias or name\n"
        "- Age: (guess a range)\n"
        "  Citation: “quoted Reddit text here”\n"
        "- Occupation:\n"
        "  Citation: “quoted Reddit text here”\n"
        "- Status:\n"
        "  Citation: “quoted Reddit text here”\n"
        "- Location:\n"
        "  Citation: “quoted Reddit text here”\n"
        "- Tier:\n"
        "  Citation: “quoted Reddit text here”\n"
        "- Archetype:\n"
        "  Citation: “quoted Reddit text here”\n"
        "- Tags: [Practical, Adaptable, Spontaneous, etc.]\n\n"
        "## Motivations\n"
        "- Convenience: [1–5]\n"
        "  Citation: “...”\n"
        "- Wellness: [1–5]\n"
        "  Citation: “...”\n"
        "... etc.\n\n"
        "## Behaviour & Habits\n"
        "• Description of habit\n"
        "  Citation: “...”\n\n"
        "## Frustrations\n"
        "• Stated frustration\n"
        "  Citation: “...”\n\n"
        "## Personality\n"
        "- Introvert vs Extrovert: [0–5]\n"
        "  Citation: “...”\n"
        "... etc.\n\n"
        "## Goals & Needs\n"
        "• Description of goal\n"
        "  Citation: “...”\n\n"
        f"Reddit Activity:\n\n{user_text}"
    )

