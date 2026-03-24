import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_INSTRUCTION = """
You are a helpful assistant who helps users with their queries related
to studies, roadmaps for learning different techstacks and career roadmaps.
You greet all with warmth and answer questions very politely.
You ask follow up questions to users if needed.
"""

conversation_history = []

def chat():
    user_query = input("\nYou: ").strip()

    if user_query.lower() in ("exit", "quit", "bye"):
        print("\nAssistant: Goodbye! Best of luck on your learning journey!\n")
        return False

    if not user_query:
        return True

    conversation_history.append({"role": "user", "content": user_query})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": SYSTEM_INSTRUCTION}] + conversation_history,
    )

    assistant_reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    print(f"\nAssistant: {assistant_reply}")
    return True


print("=" * 60)
print("  Study & Tech Stack Learning Assistant")
print("  Type 'exit' or 'quit' to end the session.")
print("=" * 60)

while True:
    if not chat():
        break