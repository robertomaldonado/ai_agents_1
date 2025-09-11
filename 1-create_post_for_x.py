import os
import sys
from typing import Optional

from openai import OpenAI
from dotenv import load_dotenv

# Send the user's message to OpenAI and return the assistant's reply text.


def ask_openai(client: OpenAI, user_message: str) -> str:
  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system",
            "content": """You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).
            Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
            Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).
            Keep the post short (200 words max) and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.
            """},
          {"role": "user",
           "content": f"""Here's the topic provided by the user for which you need to generate a post:
            <user_message>
            {user_message}
            </user_message>"""
           },
      ],
      # temperature=0.7,
  )
  return response.choices[0].message.content or ""


def validate_api_key(api_key: str) -> None:
  if not api_key:
    print("Error: Could not find an OpenAI API key.")
    print("Set OPENAI_API_KEY, or create a .env with OPENAI_API_KEY=..., or place your key in .openai_key (or set OPENAI_API_KEY_FILE).")
    sys.exit(1)


def validate_prompt(prompt: str) -> None:
  if not prompt:
    print("No input provided. Exiting.")
    sys.exit(1)


def generate_post(client: OpenAI, prompt: str) -> str:
  try:
    reply = ask_openai(client, prompt)
  except Exception as exc:  # surfaced for quickstart ergonomics
    print(f"Request failed: {exc}")
    sys.exit(1)

  return reply

# CLI entry point: obtain API key, prompt for input, call OpenAI, print reply.


def main() -> None:
  load_dotenv()
  client = OpenAI()

  prompt = input("Topic to generate a post: ").strip()
  validate_prompt(prompt)

  reply = generate_post(client, prompt)
  print(f"\nPost:\n{reply}\n")


if __name__ == "__main__":
  main()
