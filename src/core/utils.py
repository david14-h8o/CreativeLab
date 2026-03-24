import random

def pick_random(items):
    return random.choice(items)

def format_response(text: str) -> str:
    return f"✨ {text} ✨"
