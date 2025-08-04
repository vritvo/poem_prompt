POEM_URL = "https://www.poetryfoundation.org/poems/poem-of-the-day"

# Example poems and prompts for the AI instruction
EXAMPLE_POEM_1 = {
    "content": """Example 1: 

Author: Louise Glück | Title: First Memory
Long ago, I was wounded. I lived
to revenge myself
against my father, knot
for what he was—
for what I was: from the beginning of time,
in childhood, I thought
that pain meant
I was not loved.
It meant I loved.""",
    "prompt": "In this poem, the poet remembers childhood pain and connects it to love—a confusing mix where hurt feels like both proof of love and proof of its absence. The poem doesn’t solve this contradiction; it just sits with it. \nPrompt: Write a poem about a moment when love, family, or closeness carried conflicting meanings for you. Let the contradiction stay unresolved. Put both truths on the page without trying to make them fit together."
}

EXAMPLE_POEM_2 = {
    "content": """Example 2: 

Author: William Carlos Williams | Title: This Is Just to Say

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
and so cold""",
    "prompt": "This poem feels like it wasn’t meant to be a poem at all—it reads like a quick note left on the fridge, but it hints at something bigger underneath \nPrompt: Write a poem that looks like an everyday message—a text, a voicemail, a shopping list, a receipt, a subject line. Keep it brief, but let it suggest a whole relationship or moment just below the surface."
}

# Base prompt template
BASE_PROMPT_TEMPLATE = """You are a creative writing teacher. 

Provide a writing prompt about the following poem. 
It should contain a couple sentences (< 3) about the inspiration poem, as well as the prompt itself for a {genre}. 
The sentences and prompt should riff off some aspect of the poem, whether it's the content, the emotions, the structure, the lyricism, the sonic quality etc--whatever seems to be the richest source for a creative writing prompt given this particular poem.
The assignment result may not be exactly like the source-- the source poem is just inspiration.
The Prompt should be appropriate for what you'd imagine a creative writing teacher would give. But keep your language straightforward, concise, and free from flowery language. Importantly, make sure not to overstep, and infer context you don't know to be true about the poem. Stick to what you can feel confident about in the poem, even if limited. And if you do refer to the poet, just refer to them as the "poet". If you do want to give an interpetation, you can say the poem *can* be read a certain way. For example: 

{example_poem1} 

{example_prompt1} 

{example_poem2} 

{example_prompt2} 

------

You may see some unicode in the poem which you can ignore except for what it signifies re: spacing etc.Here is the real poem now to use for the context sentence(s) + prompt: 

AUTHOR: {author} 
TITLE: {title} 
POEM: 
 {poem}"""

# API Configuration
OPENAI_MODEL = "gpt-4.1"

# Default settings
DEFAULT_GENRE = "poem"
