import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class OpenAILLM:
    def __init__(self):
        api_key = os.getenv("openai-gpt3-api")
        self.client = OpenAI(api_key=api_key)

    def interact(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="davinci-002",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=15,
            temperature=0.2
        )
        return response.choices[0].message['content'].strip()
    
print(OpenAILLM().interact('Hello'))