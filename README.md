# Poem Prompt Generator
Generates a writing prompt based on a randomly selected poem. 

# Why make this? 
One good source of prompts for poems is other poems -- not to mimic the poem directly, but to use aspects of the content, emotions, structure, or sonic qualities to generate your own writing. This repo serves as a tool for generating these kinds of prompts using LLMs.


# How does this work? 
Gets a random poem from poems.db, and then generates a prompt with openAI. 

# Examples: 

## Example 1:

AUTHOR: Edgar Allan Poe 
TITLE: A Dream 

```
 In visions of the dark night
  I have dreamed of joy departed--
But a waking dream of life and light
  Hath left me broken-hearted.

Ah! what is not a dream by day
  To him whose eyes are cast
On things around him with a ray
  Turned back upon the past?

That holy dream--that holy dream,
  While all the world were chiding,
Hath cheered me as a lovely beam,
  A lonely spirit guiding.

What though that light, thro' storm and night,
  So trembled from afar--
What could there be more purely bright
  In Truth's day star?
```

AI Output: 

Poe’s “A Dream” blurs the boundary between night-dreams and waking life, suggesting that memory and longing can make reality feel ghostly or surreal. The poem finds hope and beauty in something fragile and distant, casting light into darkness but never erasing it entirely.  

Prompt: Write a poem that explores the interplay between memory and the present, where the past casts shadows or light on your current life. Let your poem move between “waking” and “dreaming”—literal or metaphorical—drawing images from both to create an emotional landscape that is neither wholly real nor wholly imagined.

## Example 2: 
```
That's the cuckoo, you say. I cannot hear it.
When last I heard it I cannot recall; but I know
Too well the year when first I failed to hear it---
It was drowned by my man groaning out to his sheep 'Ho! Ho!'

Ten times with an angry voice he shouted
'Ho! Ho!' but not in anger, for that was his way.
He died that Summer, and that is how I remember
The cuckoo calling, the children listening, and me saying, 'Nay'.

And now, as you said, 'There it is!’ I was hearing
Not the cuckoo at all, but my man's 'Ho! Ho!' instead.
And I think that even if I could lose my deafness
The cuckoo's note would be drowned by the voice of my dead.  
```
AI Output:

Edward Thomas’s poem “The Cuckoo” circles around the idea of memory and how certain sounds become tangled with loss. The cuckoo’s call, once familiar, is now inseparable from a louder memory—the voice of someone lost—so that even if he could hear, he wouldn’t hear the bird as he used to.

Prompt: Write a poem where a sound, scent, or image is forever linked to a personal loss or change. Let the sensory detail carry both the memory of what once was and the reality of what is now. Show how the thing you sense is no longer simple, but tangled with your own story.

# How to use
* Set up virtual environment
* `pip install -r requirements.txt`
* Set up an Open AI key and put it in a .env file, in the form `OPENAI_API_KEY=<key>`
* Run `python main.py`