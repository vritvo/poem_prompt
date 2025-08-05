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
    
    resp = requests.get(POEM_URL)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Get the container that contains the title, author, and poem
    poem_container = soup.find('div', class_='col-span-full')
    
    # 1) Get the title
    title_div = poem_container.find('h4', class_='type-gamma')
    title = title_div.get_text(strip=True)
    
    # 2) Get the author
    author_div = poem_container.find('div', class_='type-kappa')
    
    # Try to find the span containing the author name
    author_span = author_div.find('span')
    if author_span:
        # Extract text from the span (which should contain just the author name)
        author = author_span.get_text(strip=True)
    else:
        # Fallback: extract all text and remove "By" if present
        author_text = author_div.get_text(strip=True)
        if author_text.startswith('By '):
            author = author_text[3:]  # Remove "By " prefix
        else:
            author = author_text
      
    # 3) Get the poem
    lines_container =  title_div.parent.next_sibling
    poem_lines = []
    
    # depending on the poem, the lines container may be a div or a p. So we need to just iterate over them all. 
    for child in lines_container.find_all(recursive=False):
        text = child.get_text(strip=True)
        if text:
            poem_lines.append(text)

    # join lines; add stanza breaks
    poem = "\n\n".join(poem_lines)
    
    return {
        "title": title,
        "author": author,
        "poem": poem
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
    
    