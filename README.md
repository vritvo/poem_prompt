# Poem Prompt Generator
Generates a writing prompt based on a randomly selected poem. 

# How does this work? 
Gets a random poem and then generates a prompt for a writing exercise with openAI. 

# Example

AUTHOR: Emily Dickinson
TITLE: I heard a Fly buzz - when I died 

```
I heard a Fly buzz - when I died -
The Stillness in the Room
Was like the Stillness in the Air -
Between the Heaves of Storm -

The Eyes around - had wrung them dry -
And Breaths were gathering firm
For that last Onset - when the King
Be witnessed - in the Room -

I willed my Keepsakes - Signed away
What portion of me be
Assignable - and then it was
There interposed a Fly -

With Blue - uncertain - stumbling Buzz -
Between the light - and me -
And then the Windows failed - and then
I could not see to see -
```

AI Output: 

```
The poet describes the moment of death, focusing not on grand emotions but on small, ordinary details—like the buzz of a fly interrupting solemn silence. The poem’s calm tone, vivid sounds, and ordinary interruptions create an unexpected contrast with the seriousness of death.

Prompt: Write a poem about a moment that’s supposed to be important or dramatic, but let an everyday sensory detail—like a sound, a smell, or a small movement—break through and take over. Notice how this detail changes the mood or meaning of the moment.
```


# How to use
* `uv synv`
* Set up an Open AI key and put it in a .env file, in the form `OPENAI_API_KEY=<key>`
* Run `uv run  main.py`