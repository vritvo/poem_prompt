import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from pprint import pprint

def query_openai(input_str):
    
    load_dotenv()
    api_key=os.getenv('OPENAI_API_KEY')
    print(api_key)
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4.1",
        input=input_str
    )
    print(response.output_text)
    return response
    


def get_random_poem(max_lines=50): 
    
    found_short_poem = False
    while found_short_poem == False:
        random_poem = requests.get("https://poetrydb.org/random")
        random_poem = random_poem.json()
        random_poem = random_poem[0]
        
        if int(random_poem['linecount'])>max_lines:
            continue

        return random_poem

def get_ozymandius():
    poem = requests.get("https://poetrydb.org/title/Ozymandias/lines.json")

    return poem.json()[0]

def generate_prompt(random_poem):
    
    example_poem1 = """Example 1: \n\nAuthor: Louise Glück | Title: First Memory
Long ago, I was wounded. I lived
to revenge myself
against my father, not
for what he was—
for what I was: from the beginning of time,
in childhood, I thought
that pain meant
I was not loved.
It meant I loved."""

    example_prompt1 = "Glück’s poem holds a complicated emotional truth: pain becomes proof of both love and lack of love. This paradox gives the poem its charge, turning a memory into an unstable, shifting understanding of what relationships mean. \nPrompt: Write a poem that dwells in emotional contradiction—a moment when two truths about love, family, or intimacy existed at once and could not be untangled. Let your poem resist resolution; let both truths breathe on the page without forcing them to agree."

    example_poem2 = """Example 2: \n\nAuthor: William Carlos Williams | Title: This Is Just to Say

I have eaten
the plums
that were in
the icebox

and which
you were probably
saving
for breakfast

Forgive me
they were delicious
so sweet
and so cold"""

    example_prompt2 = "Part of the power of This Is Just to Say is that it feels like it wasn't meant to be a poem at all—it could have been pulled from a refrigerator door. \nPrompt: Write a poem in the shape of a \"non-poem\"—a voicemail transcription, an email subject line, a to-do list, a receipt, or any other utilitarian document. Let the structure of that form guide how the poem unfolds. Keep it short, but suggest a whole relationship or situation hiding underneath the surface of that format."

    poem_prompt = "You are a creative writing teacher. \n\nProvide a writing prompt about the following poem. \nIt should contain a couple sentences (< 3) about the inspiration poem, as well as the prompt itself for a {genre}. \nThe sentences and prompt should riff off some aspect of the poem, whether it's the content, the emotions, the structure, the lyricism, the sonic quality etc--whatever seems to be the richest source for a creative writing prompt given this particular poem.\nThe assignment result may not be exactly like the source-- the source poem is just inspiration.\nThe Prompt should be appropriate for what you'd imagine a creative writing teacher would give. For example: \n\n{example_poem1} \n\n{example_prompt1} \n\n{example_poem2} \n\n{example_prompt2} \n\n------\n\n  Here is the real poem now to use for the context sentence(s) + prompt: \n\nAUTHOR: {author} \nTITLE: {title} \n\n {poem}"
    
    return poem_prompt.format(
        genre="poem",
        example_poem1=example_poem1,
        example_prompt1=example_prompt1,
        example_poem2=example_poem2,
        example_prompt2=example_prompt2,
        author=random_poem["author"],
        title=random_poem["title"],
        poem="\n".join(random_poem["lines"]))
    
if __name__ == "__main__":

    # Get poem and generate AI Prompt
    random_poem = get_random_poem(max_lines=40)
    prompt = generate_prompt(random_poem)
    print(prompt)
    
    # Get poem prompt
    poetry_prompt = query_openai(prompt)
    
    print(poetry_prompt.output_text)
    
    