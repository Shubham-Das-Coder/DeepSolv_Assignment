from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Instantiate the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def query_gpt3(question, context):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Context: {context}"},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    context = "Provide some context here."
    question = "What is Apple Vision Pro?"
    print(query_gpt3(question, context))
