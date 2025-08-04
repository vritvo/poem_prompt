import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from config import (
    EXAMPLE_POEM_1, 
    EXAMPLE_POEM_2, 
    BASE_PROMPT_TEMPLATE,
    OPENAI_MODEL,
    POEM_URL
)

def scrape_poem_of_the_day():
    """Scrape the current poem of the day from Poetry Foundation."""
    response = requests.get(POEM_URL)
    soup = BeautifulSoup(response.text)
    title = soup.find('h4', {"class":"type-gamma"})
    author = title.next_sibling.next_sibling.get_text()
    poem_container = title.parent.next_sibling
    poem_paragraphs = poem_container.find_all('p')
    
    # Combine all poem paragraphs into a single text
    poem_lines = []
    for p in poem_paragraphs:
        text = p.get_text().strip()
        if text: 
            poem_lines.append(text)
    
    poem = '\n\n'.join(poem_lines)  # Join with double newlines to preserve stanza breaks
    
    return {
        'title': title.get_text(),
        'author': author,
        'poem': poem
    }


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

def _extract_poem_text(poem):
    """Extract poem text dynamically based on the poem source."""
    if 'poem' in poem:
        # Scraped poem has 'poem' field
        return poem['poem']
    elif 'lines' in poem:
        # poems.db poem has 'lines' field
        return '\n'.join(poem['lines'])
    
    
def generate_prompt(poem, genre="poem"):
    """Generate a prompt using the poem"""
    poem_text = _extract_poem_text(poem)
    
    return BASE_PROMPT_TEMPLATE.format(
        genre=genre,
        example_poem1=EXAMPLE_POEM_1["content"],
        example_prompt1=EXAMPLE_POEM_1["prompt"],
        example_poem2=EXAMPLE_POEM_2["content"],
        example_prompt2=EXAMPLE_POEM_2["prompt"],
        author=poem["author"],
        title=poem["title"],
        poem=poem_text
    )

def main():
    # Get poem and generate AI Prompt
    #poem = get_random_poem(max_lines=50)
    poem = scrape_poem_of_the_day()
    prompt = generate_prompt(poem)
    # Display the original poem
    print("Poem:\n")
    print(f"'{poem['title']}' by {poem['author']}\n")
    print(_extract_poem_text(poem))
    print("\n" + "="*50 + "\n")
    
    
    # Get poem prompt from OpenAI
    poetry_prompt = query_openai(prompt)
    
    print("AI Response:")
    print(poetry_prompt.output_text)
    
if __name__ == "__main__":
    main()
    
    