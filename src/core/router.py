from src.text import story_generator, poem_generator, joke_generator
from src.music import melody_generator
from src.art import ascii_art

def route_query(user_input: str) -> str:
    user_input = user_input.lower()

    if "story" in user_input:
        return story_generator.generate_story()
    elif "poem" in user_input:
        return poem_generator.generate_poem()
    elif "joke" in user_input:
        return joke_generator.get_joke()
    elif "melody" in user_input:
        return str(melody_generator.generate_melody("C"))
    elif "ascii" in user_input:
        return ascii_art.generate_ascii("tree")
    else:
        return "🤔 I’m not sure how to handle that yet."
