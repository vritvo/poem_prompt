import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from config import (
    EXAMPLE_POEM_1, 
    EXAMPLE_POEM_2, 
    BASE_PROMPT_TEMPLATE,
    OPENAI_MODEL,
)

def query_openai(input_str):
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')    
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=input_str
    )
    return response

def get_random_poem(max_lines=50): 
    found_short_poem = False
    while not found_short_poem:
        random_poem = requests.get("https://poetrydb.org/random")
        random_poem = random_poem.json()
        random_poem = random_poem[0]
        
        if int(random_poem['linecount']) > max_lines:
            continue

        return random_poem


def get_ozymandias():
    poem = requests.get("https://poetrydb.org/title/Ozymandias/lines.json")
    return poem.json()[0]

def generate_prompt(random_poem, genre="poem"):
    """Generate a prompt using the random poem and configuration examples."""
    return BASE_PROMPT_TEMPLATE.format(
        genre=genre,
        example_poem1=EXAMPLE_POEM_1["content"],
        example_prompt1=EXAMPLE_POEM_1["prompt"],
        example_poem2=EXAMPLE_POEM_2["content"],
        example_prompt2=EXAMPLE_POEM_2["prompt"],
        author=random_poem["author"],
        title=random_poem["title"],
        poem="\n".join(random_poem["lines"])
    )

def main():
    # Get poem and generate AI Prompt
    random_poem = get_random_poem(max_lines=50)
    prompt = generate_prompt(random_poem)
    
    # Display the original poem
    print("Poem:\n")
    print(f"'{random_poem['title']}' by {random_poem['author']}\n")
    print("\n".join(random_poem["lines"]))
    print("\n" + "="*50 + "\n")
    
    # Get poem prompt from OpenAI
    poetry_prompt = query_openai(prompt)
    
    print("AI Response:")
    print(poetry_prompt.output_text)

if __name__ == "__main__":
    main()
    
    