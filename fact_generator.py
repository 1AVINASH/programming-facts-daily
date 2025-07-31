import os
import json
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
HISTORY_DIR = "chat_histories"
FACTS_DIR = "facts"
MODEL = "gpt-4"  # or gpt-3.5-turbo

os.makedirs(HISTORY_DIR, exist_ok=True)

@dataclass
class FactGeneratorInput:
    subject: str
    level: Optional[str] = "INTERMEDIATE"


class Levels:
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    PROFESSIONAL = "professional"

class FactGenerator:
    def __init__(self, input: FactGeneratorInput):
        self.subject = input.subject.lower()
        self.expertise_level = input.level.lower()

    def get_history_path(self) -> str:
        return os.path.join(HISTORY_DIR, f"{self.subject.replace(' ', '_')}.json")

    def get_facts_path(self) -> str:
        return os.path.join(FACTS_DIR, f"{self.subject.replace(' ', '_')}.md")

    def load_chat_history(self):
        path = self.get_history_path()
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        return [{"role": "system", "content": f"You are an expert on {self.subject}. This subject will only be related to computer science. You can add code as well if required. This output should be in markdown format. Give one unique information daily that hasn't been mentioned before."}]

    def save_chat_history(self, history):
        path = self.get_history_path()
        with open(path, 'w') as f:
            json.dump(history, f, indent=2)

    def save_fact(self, assistant_reply):
        path = self.get_facts_path()
        now = datetime.now()
        datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(path, 'a') as f:
            f.write("\n"*2)
            f.write("---\n")
            f.write(f"{datetime_string} \n ---")
            f.write(assistant_reply)
            f.write("\n---\n")
            f.write("\n"*2)

    def get_fact(self):
        history = self.load_chat_history()

        # Append user prompt
        history.append({"role": "user", "content": f"Give me one unique information related to this topic. Assume my expertise level is {self.expertise_level} at the moment and tweak your response respectively"})

        response = client.chat.completions.create(
            model=MODEL,
            messages=history,
            temperature=0.7
        )
        assistant_reply = response.choices[0].message.content.strip()

        # Append assistant response to history
        history.append({"role": "assistant", "content": assistant_reply})

        self.save_chat_history(history)
        self.save_fact(assistant_reply)

        return assistant_reply